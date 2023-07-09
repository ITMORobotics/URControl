# URControl

    docker build -t ur .

    docker run --rm -ti --net host -v ./examples:/workspace/examples ur

# Required
ur_rtde requires a real-time kernel. You can use an instruction, for example
[real-time-setup-guide](https://sdurobotics.gitlab.io/ur_rtde/guides/guides.html#real-time-setup-guide) from ur_rtde docs.

You can start without real-time kernel, but this may lead to an unexpected stop during operation.