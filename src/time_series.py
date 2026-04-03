from pathlib import Path
import pandas as pd


def grouped_summary(df, group_col, value_col, report_dir=None):
    """
    Group by one column and summarize a numeric column.

    Parameters:
    - df: pandas DataFrame
    - group_col: column to group by (categorical)
    - value_col: numeric column to summarize
    - report_dir: optional directory to save output

    Returns:
    - dict with text + artifact paths
    """

    # Check columns exist
    if group_col not in df.columns:
        raise ValueError(f"Column not found: {group_col}")
    if value_col not in df.columns:
        raise ValueError(f"Column not found: {value_col}")

    # Create summary
    summary = (
        df.groupby(group_col)[value_col]
        .agg(["count", "mean", "median", "min", "max"])
        .reset_index()
    )

    artifact_paths = []

    # Save output if report_dir provided
    if report_dir is not None:
        report_dir = Path(report_dir)
        report_dir.mkdir(parents=True, exist_ok=True)

        out_path = report_dir / f"grouped_summary_{group_col}_{value_col}.csv"
        summary.to_csv(out_path, index=False)

        artifact_paths.append(str(out_path))

    text = f"Grouped summary of '{value_col}' by '{group_col}' created successfully."

    return {
        "text": text,
        "artifact_paths": artifact_paths,
        "preview": summary.head().to_dict(orient="records"),
    }