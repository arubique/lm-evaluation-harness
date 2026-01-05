# HellaSwag Prompts Task

This task evaluates models on HellaSwag multiple-choice questions loaded from a JSON file with pre-formatted prompts.

## Task Configuration

- **Task Name**: `hellaswag_prompts`
- **Task Type**: Multiple Choice
- **Dataset Source**: Local JSON file
- **Number of Examples**: 10,042

## Dataset Format

The dataset is loaded from a JSON file containing multiple-choice questions from HellaSwag. Each example includes:

- `query`: The question/context text that needs to be completed
- `choices`: List of 4 possible completion options
- `gold`: The 0-indexed index of the correct answer
- `example`: Same as query (for reference)
- `full_prompt`: Full prompt with few-shot examples (for reference)

## Task Description

HellaSwag is a commonsense reasoning task that requires models to choose the most appropriate continuation for a given context. The task tests a model's understanding of everyday situations and common sense.

## Evaluation Metrics

- **Accuracy (acc)**: Standard accuracy metric
- **Normalized Accuracy (acc_norm)**: Normalized accuracy metric

## Usage

To evaluate a model on this task:

```bash
lm_eval --model <model> --tasks hellaswag_prompts --num_fewshot 0
```

To view the task prompts:

```bash
python -m scripts.write_out --output_base_path <path> --tasks hellaswag_prompts --sets test --num_fewshot 0 --num_examples 5
```

## Configuration Details

The task is configured to:
- Load data from a local JSON file
- Use the `query` field as the input prompt
- Use the `choices` field for multiple choice options (4 choices per question)
- Use the `gold` field (0-indexed) as the correct answer
- Evaluate on all examples in the dataset

## Differences from Standard HellaSwag

This task uses a custom JSON file with pre-formatted prompts, while the standard `hellaswag` task loads from the HuggingFace dataset `Rowan/hellaswag` and includes preprocessing steps.

## Version History

- **Version 1.0** (Initial version): Basic multiple-choice HellaSwag task configuration with prompts
