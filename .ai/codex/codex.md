# AI Codex

## Usage

- Review: @codex.md (silent load, no output)
- Update: @learn.md
- File paths: Always use absolute paths from project root

## Errors

E000:

- Context: [Relevant project area or file]
- Error: [Precise description]
- Correction: [Exact fix]
- Prevention: [Specific strategy]
- Related: [IDs of related errors/learnings]

E001: Poetry Installation Error
- Context: Backend setup, Task-2
- Error: Unspecified error during Poetry installation or initialization
- Correction: To be determined after gathering more information
- Prevention: Implement a more robust error handling and reporting system during the setup process
- Related: None yet

E002: Poetry Project Installation Error
- Context: Backend setup, Task-2, `poetry install` command
- Error: "The current project could not be installed: [Errno 2] No such file or directory: 'C:\\Users\\Silo\\Desktop\\Projects\\Job-Search\\Job-Search\\backend\\README.md'"
- Correction: Create a README.md file in the backend directory or configure Poetry to not require it
- Prevention: Ensure all required files are present before running `poetry install`, or configure Poetry to not require optional files
- Related: E001, L001

E003: Directory Creation Error
- Context: Backend setup, Task-2, creating subdirectories
- Error: "mkdir: A positional parameter cannot be found that accepts argument 'app/core'."
- Correction: Use separate mkdir commands for each directory or use an alternative method for directory creation
- Prevention: Use OS-agnostic methods for directory creation or check OS before running specific commands
- Related: None

E004: Invalid PATH Variable Reference
- Context: Configuring development environment, Task-4
- Error: "ParserError: Variable reference is not valid. ':' was not followed by a valid variable name character. Consider using ${} to delimit the name."
- Correction: Modify the PATH export command to use proper syntax for the shell being used
- Prevention: Test shell commands in the specific environment before adding them to configuration files
- Related: L004

E005: Incorrect FastAPI Application Initialization
- Context: Backend setup, Task-6, initializing FastAPI application in `app/main.py`
- Error: String literal is unterminated, and PowerShell command is mixed with Python code
- Correction: Separate PowerShell command from Python code and properly format the Python script
- Prevention: Use separate steps for creating the file and writing its contents, and validate the content before saving
- Related: None

E006: PowerShell Command in Python File
- Context: Backend setup, Task-6, creating `app/main.py`
- Error: PowerShell command (`@"` and `"@ | Set-Content`) is included in the Python file content
- Correction: Remove PowerShell command syntax and keep only the Python code
- Prevention: Clearly separate PowerShell commands used for file creation from the actual file content
- Related: E005, L007

E007: Missing Pydantic Settings Module
- Context: Backend setup, Task-7, running FastAPI application
- Error: ModuleNotFoundError: No module named 'pydantic_settings'
- Correction: Install pydantic-settings package or update Pydantic to version 2.0 or higher
- Prevention: Ensure all required dependencies are listed in pyproject.toml and installed
- Related: None

E008: FastAPI Endpoint Not Found
- Context: Testing POST /jobs endpoint, Task-7
- Error: HTTP 404 Not Found when attempting to create a new job
- Correction: Verify that the /jobs POST endpoint is correctly defined in the FastAPI application
- Prevention: Implement endpoint verification tests as part of the development process
- Related: None

E009: Missing Pydantic Settings Import
- Context: Backend setup, config.py file
- Error: Import "pydantic_settings" could not be resolved
- Correction: Install pydantic-settings package or update import statement based on Pydantic version
- Prevention: Ensure all required packages are listed in requirements.txt or pyproject.toml and installed
- Related: E007, L009

E010: Pydantic BaseSettings Import Error
- Context: Backend setup, config.py file
- Error: PydanticImportError: `BaseSettings` has been moved to the `pydantic-settings` package
- Correction: Update import statement to use pydantic_settings instead of pydantic for BaseSettings
- Prevention: Keep up-to-date with Pydantic version changes and their impact on imports
- Related: E009, L009, L011

E011: Pydantic BaseSettings Import Error
- Context: backend/app/core/config.py
- Error: PydanticImportError: `BaseSettings` has been moved to the `pydantic-settings` package
- Correction: Update the import statement to use pydantic_settings instead of pydantic for BaseSettings
- Prevention: Keep up-to-date with Pydantic version changes and their impact on imports
- Related: E009, L009, L011

E001: ImportError in FastAPI Startup
- Context: backend/app/main.py and backend/app/core/config.py
- Error: ImportError: cannot import name 'get_settings' from 'app.core.config'
- Correction: Add the missing `get_settings` function to the config.py file
- Prevention: Always ensure that all functions and classes referenced in import statements are properly defined in their respective modules
- Related: None

E012: Supabase Table Not Found
- Context: backend/app/main.py, /test-supabase endpoint
- Error: Supabase connection failed: relation "public.your_table_name" does not exist
- Correction: Create the necessary table in Supabase or update the endpoint to use an existing table
- Prevention: Ensure all required database tables are created before testing endpoints, and use actual table names in test queries
- Related: None

## Learnings

L000:

- Context: [Relevant project area or file]
- Insight: [Concise description]
- Application: [How to apply this knowledge]
- Impact: [Potential effects on project]
- Related: [IDs of related errors/learnings]

L001: Error Reporting Importance
- Context: Backend setup, Task-2
- Insight: Detailed error reporting is crucial for remote troubleshooting and problem-solving
- Application: Implement a standardized error reporting format for all tasks, including error messages, error codes, and context
- Impact: Improved ability to diagnose and resolve issues quickly, enhancing overall project efficiency
- Related: E001

L002:

- Context: Project architecture
- Insight: Repository pattern for data access
- Application: '/src' is root, '/src/auth' for authentication, '/src/database' for data access
- Impact: Organized code structure, separation of concerns
- Related: None

L003: Poetry Project Configuration
- Context: Backend setup, Task-2
- Insight: Poetry attempts to install the current project by default and looks for certain files (like README.md)
- Application: Either create necessary project files or configure Poetry to not install the current project if it's not needed
- Impact: Smoother project setup and dependency management
- Related: E003

L004: OS-Specific Command Differences
- Context: Backend setup, Task-2
- Insight: Command syntax, especially for directory creation, can vary between operating systems
- Application: Use OS-agnostic methods or provide alternative commands for different operating systems
- Impact: Improved cross-platform compatibility in setup scripts and instructions
- Related: E004

L005: Shell-Specific Syntax
- Context: Configuring development environment, Task-4
- Insight: Different shells (bash, zsh, PowerShell) have different syntax for environment variable manipulation
- Application: Provide alternative commands for different shells or use a more universal method for PATH manipulation
- Impact: Improved cross-platform compatibility and easier setup process for different development environments
- Related: E004, L004

L006: Terminal Restart for Environment Changes
- Context: Troubleshooting pre-commit installation and PATH configuration, Task-4
- Insight: Some environment changes, particularly PATH modifications, may require restarting the terminal to take effect
- Application: After making changes to environment variables or system PATH, advise users to restart their terminal or IDE
- Impact: Ensures that new environment configurations are properly loaded and applied
- Related: E004, L005

L007: Separating File Creation and Content Writing
- Context: Backend setup, Task-6, creating `app/main.py`
- Insight: When creating files with content, it's better to separate the file creation step from the content writing step
- Application: Use separate commands to create the file and to write its contents, allowing for better error checking and formatting
- Impact: Reduces the risk of syntax errors and improves code readability and maintainability
- Related: E005

L008: Clear Separation of Shell Commands and File Content
- Context: Backend setup, Task-6, creating `app/main.py`
- Insight: When using shell commands to create files with content, it's crucial to clearly separate the command syntax from the intended file content
- Application: Use shell commands only for file operations, and keep the file content clean of any shell-specific syntax
- Impact: Ensures the created files contain only the intended content, improving code quality and preventing runtime errors
- Related: E005, E006, L007

L009: Pydantic Version Compatibility
- Context: Backend setup, Task-7, configuring Supabase
- Insight: Pydantic 2.0+ separates settings functionality into a separate package
- Application: When using Pydantic for settings, ensure compatibility with the installed version or install additional required packages
- Impact: Ensures proper functionality of configuration management in the application
- Related: E007

L010: API Endpoint Verification
- Context: Testing FastAPI endpoints, Task-7
- Insight: Endpoints may not be accessible even if the server is running, possibly due to incorrect routing or implementation
- Application: Implement a systematic approach to verify all API endpoints after creation or modification
- Impact: Ensures that all intended API functionalities are correctly exposed and reduces debugging time
- Related: E008

L011: Pydantic Settings Module Changes
- Context: Backend setup, config.py file
- Insight: Pydantic has separated its settings functionality into a separate package in newer versions
- Application: When using Pydantic for settings, check the installed version and use the appropriate import statement
- Impact: Ensures compatibility with different versions of Pydantic and prevents import errors
- Related: E009, L009

L012: Pydantic Version 2.x Breaking Changes
- Context: Backend setup, config.py file
- Insight: Pydantic 2.x has made significant changes to its structure, moving certain functionalities to separate packages
- Application: When upgrading Pydantic, carefully review the migration guide and update import statements accordingly
- Impact: Ensures compatibility with the latest Pydantic versions while maintaining correct functionality
- Related: E010, L009, L011

L013: Pydantic 2.x Breaking Changes - BaseSettings
- Context: Backend setup, config.py file
- Insight: Pydantic 2.x has moved BaseSettings to a separate package called pydantic-settings
- Application: When using BaseSettings, import it from pydantic_settings instead of pydantic
- Impact: Ensures compatibility with the latest Pydantic versions while maintaining correct functionality for settings management
- Related: E010, E011, L009, L011, L012

L014: Supabase Table Creation and Management
- Context: Backend setup, Supabase integration
- Insight: Database tables need to be explicitly created in Supabase before they can be queried
- Application: Create necessary tables in Supabase before testing database connections or queries
- Impact: Ensures smooth integration between the application and the Supabase database
- Related: E012
