#!/usr/bin/python3

import sys
import os


def main():
    pdf_destination = os.environ.get("pdf_destination", "")
    annotation_destination = os.environ.get("annotation_destination", "")
    obsidian_vault_root = os.environ.get("obsidian_vault_root", "")
    file_source = sys.argv[1]

    obsidian_pdf_path = pdf_destination[len(obsidian_vault_root) :]

    pdf_name = file_source.split("/")[-1].split(".")[0]

    print(pdf_destination)

    print(sys.argv)

    os.rename(file_source, f"{pdf_destination}/{pdf_name}.pdf")

    with open(f"{annotation_destination}/{pdf_name}.md", "w+") as f:
        f.write(f"---\nannotation-target: {obsidian_pdf_path}/{pdf_name}.pdf\n---\n")


if __name__ == "__main__":
    main()
