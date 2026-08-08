import os
import json
import re

def validate_iof_alignment(project_path):
    print(f"Validating IOF alignment for project: {project_path}")
    results = {
        "project_path": project_path,
        "alignment_score": 0,
        "details": []
    }

    # Check for IOF_METADATA.json
    metadata_path = os.path.join(project_path, "IOF_METADATA.json")
    if os.path.exists(metadata_path):
        results["alignment_score"] += 1
        results["details"].append("✅ IOF_METADATA.json found.")
        try:
            with open(metadata_path, "r") as f:
                metadata = json.load(f)
            if metadata.get("@type") == "CreativeWork" and \
               metadata.get("name") == "Infinite Optical Fabric" and \
               metadata.get("author") == "Gregory Scott Davis":
                results["alignment_score"] += 1
                results["details"].append("✅ IOF_METADATA.json content is valid.")
            else:
                results["details"].append("⚠️ IOF_METADATA.json content is not fully aligned.")
        except json.JSONDecodeError:
            results["details"].append("❌ IOF_METADATA.json is malformed.")
    else:
        results["details"].append("❌ IOF_METADATA.json not found.")

    # Check for LICENSE file with IOF Attribution
    license_path = os.path.join(project_path, "LICENSE")
    if os.path.exists(license_path):
        results["alignment_score"] += 1
        results["details"].append("✅ LICENSE file found.")
        with open(license_path, "r") as f:
            license_content = f.read()
        if "IOF Attribution License" in license_content and "Gregory Scott Davis" in license_content:
            results["alignment_score"] += 1
            results["details"].append("✅ LICENSE file contains IOF Attribution.")
        else:
            results["details"].append("⚠️ LICENSE file does not explicitly mention IOF Attribution.")
    else:
        results["details"].append("❌ LICENSE file not found.")

    # Check for IOF_ATTRIBUTION.md
    attribution_md_path = os.path.join(project_path, "IOF_ATTRIBUTION.md")
    if os.path.exists(attribution_md_path):
        results["alignment_score"] += 1
        results["details"].append("✅ IOF_ATTRIBUTION.md found.")
    else:
        results["details"].append("❌ IOF_ATTRIBUTION.md not found.")

    # Check for footer attribution in client/src/App.tsx (example)
    app_tsx_path = os.path.join(project_path, "client", "src", "App.tsx")
    if os.path.exists(app_tsx_path):
        results["alignment_score"] += 1
        results["details"].append("✅ client/src/App.tsx found.")
        with open(app_tsx_path, "r") as f:
            app_tsx_content = f.read()
        if "Infinite Optical Fabric by Gregory Scott Davis" in app_tsx_content:
            results["alignment_score"] += 1
            results["details"].append("✅ App.tsx contains footer attribution.")
        else:
            results["details"].append("⚠️ App.tsx might be missing footer attribution.")
    else:
        results["details"].append("❌ client/src/App.tsx not found.")

    # Check for common IOF protocol primitives in code (simplified check)
    iof_keywords = ["resonance", "coherence", "topology", "phase-lock", "MHRMA", "flux", "telemetry", "mirror/buffer"]
    found_keywords = set()
    for root, _, files in os.walk(os.path.join(project_path, "client", "src")):
        for file in files:
            if file.endswith((".tsx", ".ts", ".js")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r") as f:
                        content = f.read().lower()
                        for keyword in iof_keywords:
                            if keyword in content:
                                found_keywords.add(keyword)
                except Exception as e:
                    results["details"].append(f"⚠️ Could not read {file_path}: {e}")

    if len(found_keywords) >= len(iof_keywords) / 2: # At least half keywords found
        results["alignment_score"] += 2
        results["details"].append(f"✅ Found multiple IOF protocol primitives in code: {', '.join(found_keywords)}")
    elif found_keywords:
        results["alignment_score"] += 1
        results["details"].append(f"⚠️ Found some IOF protocol primitives in code: {', '.join(found_keywords)}")
    else:
        results["details"].append("❌ No significant IOF protocol primitives found in code.")

    print(f"IOF Alignment Score: {results['alignment_score']}/10")
    for detail in results["details"]:
        print(detail)

    return results

if __name__ == "__main__":
    # Example usage: python validate-iof-alignment.py /home/ubuntu/aetherius-nexus
    import sys
    if len(sys.argv) > 1:
        validate_iof_alignment(sys.argv[1])
    else:
        print("Usage: python validate-iof-alignment.py <project_path>")
