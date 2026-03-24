from __future__ import annotations

import argparse
from pathlib import Path

try:
    import fitz
except ImportError as exc:
    raise SystemExit(
        "PyMuPDF is required. Install it with: pip install PyMuPDF"
    ) from exc


def convert_pdf_to_png(pdf_path: Path, output_dir: Path, dpi: int = 200) -> list[Path]:
    """Convert each page of a PDF file into a PNG image."""
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    created_files: list[Path] = []
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)

    with fitz.open(pdf_path) as document:
        pdf_stem = pdf_path.stem

        for page_index in range(document.page_count):
            page = document.load_page(page_index)
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)
            output_path = output_dir / f"{pdf_stem}_page_{page_index + 1}.png"
            pixmap.save(output_path)
            created_files.append(output_path)

    return created_files


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert every page of a PDF file into PNG images."
    )
    parser.add_argument("pdf", type=Path, help="Path to the input PDF file")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        help="Directory where PNG files will be written. Defaults to <pdf_name>_pages",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=200,
        help="Rendering DPI for output images (default: 200)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    pdf_path = args.pdf.resolve()
    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else pdf_path.with_name(f"{pdf_path.stem}_pages")
    )

    created_files = convert_pdf_to_png(pdf_path, output_dir, dpi=args.dpi)

    print(f"Converted {len(created_files)} page(s) to PNG:")
    for file_path in created_files:
        print(file_path)


if __name__ == "__main__":
    main()
