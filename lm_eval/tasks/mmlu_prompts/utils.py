from typing import Any, Dict

import datasets


def load_dataset(
    use_full_prompt: bool = False,
    data_files: str | Dict[str, Any] | None = None,
    **kwargs: Any,
) -> Dict[str, datasets.Dataset]:
    """
    Custom loader for the hellaswag_prompts task.

    It loads the underlying JSON file and, if `use_full_prompt` is True
    (propagated via task metadata / CLI), replaces the `query` field with
    the longer `full_prompt` field so that `doc_to_text` can keep using
    `{{query}}` regardless of configuration.
    """

    # HuggingFace datasets will infer a single "train" split for a lone file.
    ds = datasets.load_dataset("json", data_files=data_files, split="train")

    # If the user requested full prompts, enforce that the data actually
    # contains a `full_prompt` column; otherwise this mode is invalid.
    if use_full_prompt and "full_prompt" not in ds.column_names:
        raise ValueError(
            "hellaswag_prompts: --use_full_prompt was set, but the loaded JSON "
            "does not contain a 'full_prompt' field."
        )

    if use_full_prompt:
        def _swap_query_with_full_prompt(doc: Dict[str, Any]) -> Dict[str, Any]:
            # Only swap if a full_prompt field is present.
            if "full_prompt" in doc:
                doc["query"] = doc["full_prompt"]
            return doc

        ds = ds.map(_swap_query_with_full_prompt)

    # Expose a standard split mapping for the harness.
    return {"train": ds}

