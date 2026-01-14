# Anatomy Task

This task evaluates models on anatomy multiple-choice questions.

## Task Configuration

- **Task Name**: `anatomy`
- **Task Type**: Multiple Choice
- **Dataset Source**: Local JSON file
- **Number of Examples**: 135

## Dataset Format

The dataset is loaded from a JSON file containing multiple-choice questions about anatomy. Each example includes:

- `query`: The question text with answer choices already formatted (A, B, C, D)
- `choices`: List of choice labels `["A", "B", "C", "D"]`
- `gold`: The 0-indexed index of the correct answer
- `example`: Same as query (for reference)
- `full_prompt`: Full prompt with few-shot examples (for reference)

## Evaluation Metrics

- **Accuracy (acc)**: Standard accuracy metric
- **Normalized Accuracy (acc_norm)**: Normalized accuracy metric

## Usage

To evaluate a model on this task:

```bash
lm_eval --model <model> --tasks anatomy --num_fewshot 0
```

To view the task prompts:

```bash
python -m scripts.write_out --output_base_path <path> --tasks anatomy --sets test --num_fewshot 0 --num_examples 5
```

## Configuration Details

The task is configured to:
- Load data from a local JSON file
- Use the `query` field as the input prompt
- Use the `choices` field for multiple choice options
- Use the `gold` field (0-indexed) as the correct answer
- Evaluate on all examples in the dataset

## Version History

- **Version 1.0** (Initial version): Basic multiple-choice anatomy task configuration
