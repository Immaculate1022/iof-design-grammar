import json
import os
from datetime import datetime

def generate_iof_metadata(project_path, project_name, author_name, author_location, license_name, usage_terms):
    metadata = {
        "@context": "https://schema.org/",
        "@type": "CreativeWork",
        "name": project_name,
        "author": author_name,
        "contentLocation": author_location,
        "license": license_name,
        "usageTerms": usage_terms,
        "dateCreated": datetime.now().isoformat()
    }

    output_path = os.path.join(project_path, "IOF_METADATA.json")
    with open(output_path, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"Generated IOF_METADATA.json at {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate IOF_METADATA.json for an IOF-aligned project.")
    parser.add_argument("--project_path", required=True, help="Path to the project directory.")
    parser.add_argument("--project_name", required=True, help="Name of the project (e.g., 'Infinite Optical Fabric').")
    parser.add_argument("--author_name", required=True, help="Author's name (e.g., 'Gregory Scott Davis').")
    parser.add_argument("--author_location", required=True, help="Author's location (e.g., 'Princeton, NC').")
    parser.add_argument("--license_name", default="IOF Attribution License v1.0", help="Name of the license.")
    parser.add_argument("--usage_terms", default="Attribution Required", help="Usage terms.")

    args = parser.parse_args()

    generate_iof_metadata(
        args.project_path,
        args.project_name,
        args.author_name,
        args.author_location,
        args.license_name,
        args.usage_terms
    )
