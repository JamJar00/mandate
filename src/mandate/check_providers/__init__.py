from mandate.check_providers.readme_check_provider import ReadmeCheckProvider
from mandate.check_providers.license_check_provider import LicenseCheckProvider
from mandate.check_providers.git_check_provider import GitCheckProvider
from mandate.check_providers.ci_check_provider import CiCheckProvider
from mandate.check_providers.python_check_provider import PythonCheckProvider
from mandate.check_providers.github_check_provider import GitHubCheckProvider
from mandate.check_providers.csharp_check_provider import CSharpCheckProvider
from mandate.check_providers.contributing_check_provider import ContributingCheckProvider
from mandate.check_providers.javascript_check_provider import JavascriptCheckProvider
from mandate.check_providers.rust_check_provider import RustCheckProvider
from mandate.check_providers.terraform_check_provider import TerraformCheckProvider
from mandate.check_providers.shell_check_provider import ShellCheckProvider
from mandate.check_providers.ai_instruction_check_provider import AiInstructionCheckProvider

check_providers = [
    ReadmeCheckProvider(),
    LicenseCheckProvider(),
    GitCheckProvider(),
    CiCheckProvider(),
    PythonCheckProvider(),
    GitHubCheckProvider(),
    CSharpCheckProvider(),
    ContributingCheckProvider(),
    JavascriptCheckProvider(),
    RustCheckProvider(),
    TerraformCheckProvider(),
    ShellCheckProvider(),
    AiInstructionCheckProvider(),
]
