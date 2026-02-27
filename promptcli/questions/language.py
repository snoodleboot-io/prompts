# Language registry and factory functions

# Registry of available language keys for dynamic lookup
LANGUAGE_KEYS = [
    "python",
    "typescript",
    "javascript",
    "java",
    "csharp",
    "go",
    "rust",
    "ruby",
    "php",
    "swift",
    "kotlin",
    "scala",
    "elixir",
    "elm",
    "haskell",
    "clojure",
    "fsharp",
    "dart",
    "julia",
    "lua",
    "r",
    "shell",
    "groovy",
    "terraform",
    "sql",
]


def get_language_questions(language: str):
    """
    Get all questions for a specific language.

    Returns a list of questions that should be asked for the given language.
    """
    from promptcli.questions.base import BaseQuestion

    questions: list[BaseQuestion] = []
    lang = language.lower()

    # Import here to avoid circular imports
    from promptcli.questions.python import (
        PythonFormatterQuestion,
        PythonLinterQuestion,
        PythonPackageManagerQuestion,
        PythonRuntimeQuestion,
        PythonTestFrameworkQuestion,
        PythonTestRunnerQuestion,
    )
    from promptcli.questions.typescript import (
        TypeScriptFrameworkQuestion,
        TypeScriptPackageManagerQuestion,
        TypeScriptTestFrameworkQuestion,
        TypeScriptVersionQuestion,
    )

    if lang == "python":
        questions.extend(
            [
                PythonRuntimeQuestion(),
                PythonPackageManagerQuestion(),
                PythonTestFrameworkQuestion(),
                PythonTestRunnerQuestion(),
                PythonLinterQuestion(),
                PythonFormatterQuestion(),
            ]
        )
    elif lang == "typescript" or lang == "javascript":
        questions.extend(
            [
                TypeScriptVersionQuestion(),
                TypeScriptPackageManagerQuestion(),
                TypeScriptTestFrameworkQuestion(),
                TypeScriptFrameworkQuestion(),
            ]
        )

    return questions
