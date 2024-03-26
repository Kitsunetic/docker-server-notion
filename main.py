import re
import subprocess
from dataclasses import dataclass


CMD_CONTAINER = 'docker ps -a --size --format "table {{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Size}}"'
CMD_IMAGE = "docker images"


class DockerOutput:
    def __init__(self, output: str):
        lines = output.strip().split("\n")

        # parse title
        keys = re.split(r"\s{2,}", lines[0])
        self.output = {k: [] for k in keys}

        # parse data
        for line in lines[1:]:
            data = re.split(r"\s{2,}", line)
            for key, item in zip(keys, data):
                self.output[key].append(item)

        # parse lengths
        self.key_lens = {}
        for k in keys:
            self.key_lens[k] = max([len(k)] + list(map(len, self.output[k])))

    def __len__(self):
        return len(self.output[list(self.output.keys())[0]])

    def __str__(self):
        # make title
        msg = "|"
        for k in self.output.keys():
            msg += (" {item:<%d} |" % self.key_lens[k]).format(item=k)
        msg += "\n|"
        for k in self.output.keys():
            msg += "-" * (self.key_lens[k] + 2) + "|"

        # make content
        for i in range(len(self)):
            msg += "\n|"
            for k in self.output.keys():
                msg += (" {item:<%d} |" % self.key_lens[k]).format(item=self.output[k][i])

        return msg

    def __repr__(self):
        return self.__str__()


def main():
    # image
    output = subprocess.check_output(CMD_IMAGE, shell=True, text=True)
    images = DockerOutput(output)
    print("Images:")
    print(images)
    print("\n")

    # container
    output = subprocess.check_output(CMD_CONTAINER, shell=True, text=True)
    containers = DockerOutput(output)
    print("Containers:")
    print(containers)


if __name__ == "__main__":
    main()
