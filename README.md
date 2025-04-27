# GHA: Output Function Modification and Developer Attribution Logger


## Overview

This GHA is programmed to identify modifications made to output functions within the source code and to attribute these changes to the corresponding developer based on commit metadata. It serves as a lightweight auditing tool that facilitates greater visibility into the evolution of codebases, particularly in collaborative software development environments.


## Core Functionality

- Detection of Source Code Changes: Programmatically parses recent commits to isolate modifications involving output functions.

- Developer Attribution: Extracts and logs the identity of the contributor associated with each detected change.

- Workflow Integration: Designed for seamless integration into continuous integration (CI) pipelines to enhance traceability and accountability.

## Usage Guidelines

**Prerequisites**

To ensure successful operation, the following prerequisites must be satisfied:

- The repository should follow a consistent coding standard that enables reliable detection of output functions.

- Commit history must accurately reflect the author's identity (typically configured through Git user settings).

**Run as GHA**

Replace log_dev_tracker.py with your file.

**Inputs**

This Action is designed to operate autonomously and therefore does not require any user-provided inputs.

**Outputs**

Upon execution, the Action writes the following information to the workflow logs:

- Modified Output Functions: A list of output functions identified as changed in the most recent commit(s).

- Developer Information: The Git username associated with the changes.

No formal output variables are exported to downstream steps.


## License

[MIT](https://choosealicense.com/licenses/mit/)
