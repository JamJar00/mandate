from mandate.check import Check, CheckProvider, CheckResult, Result, Severity, CheckFix
import mandate.util
import mandate.template_util
import os


class AddAiInstructionFix(CheckFix):
    def fix(self, directory, _):
        path = os.path.join(directory, "AGENTS.md")
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(mandate.template_util.template("ai_instructions.md", directory))
            return True
        except Exception:
            return False

    @property
    def success_message(self):
        return "Created AGENTS.md from template. You should edit it to describe agent behavior, constraints, and contact points."

    @property
    def failure_message(self):
        return "Tried to create AGENTS.md but was unable to."


class AiInstructionCheckProvider(CheckProvider):
    def name(self):
        return "AI Instructions"

    def test(self, directory):
        # Basenames to search for anywhere in the tree
        basenames = ["AGENTS.md", "AI_INSTRUCTIONS.md", "INSTRUCTIONS.md"]

        found_path = None
        for b in basenames:
            matches = list(mandate.util.find_files_with_name(directory, b))
            if matches:
                found_path = os.path.join(directory, matches[0])
                break

        yield CheckResult(
            "AI001",
            Result.PASSED if found_path is not None else Result.FAILED,
            file_path=found_path,
            fix=AddAiInstructionFix(),
        )

        if not found_path:
            # Can't validate sections if there's no file
            yield CheckResult("AI002", Result.PRE_REQUISITE_CHECK_FAILED)
            return

        required_sections = [
            "# Project Overview",
            "# Build and Test Commands",
            "# Code Style Guidelines",
            "# Testing Instructions",
            "# Security Considerations",
        ]

        try:
            with open(found_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            yield CheckResult("AI002", Result.FAILED, file_path=found_path)
            return

        content_lower = content.lower()
        present = all(title.lower() in content_lower for title in required_sections)

        yield CheckResult(
            "AI002",
            Result.PASSED if present else Result.FAILED,
            file_path=found_path,
        )

    def checks(self):
        return [
            Check(
                "AI001",
                Severity.MEDIUM,
                ["open-source", "inner-source", "team"],
                "Projects should include an AI instruction file (e.g., agents.md)",
                "Add an AI instruction file such as agents.md, AI_INSTRUCTIONS.md or .ai/INSTRUCTIONS.md describing AI agent behaviour, constraints, and contact points.",
            ),
            Check(
                "AI002",
                Severity.LOW,
                ["open-source", "inner-source", "team"],
                "AI instruction files should contain required sections",
                "The AI instruction file must include sections: Project Overview, Build and Test Commands, Code Style Guidelines, Testing Instructions, Security Considerations",
            ),
        ]
