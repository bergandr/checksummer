import hashlib


def sha512_file(file):
    with open(file, "rb") as f:
        digest = hashlib.file_digest(f, "sha512")
        print(f"{digest.hexdigest()}  {f.name}")
        return digest.hexdigest()


def checksum_list(file_list):
    hash_dict = {}
    for file in file_list:
        sha512 = sha512_file(file)
        hash_dict[file] = sha512

    return hash_dict
