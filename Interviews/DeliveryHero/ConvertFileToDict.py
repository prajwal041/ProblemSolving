def parse_config(config_file):
    d = {}
    with open(config_file) as f:
        lines = f.readlines()
        for item in lines:
            if item[0] != "#":
                item = item.rstrip().replace('\n', '')
                if len(item) != 0:
                    vals = item.split("=", 1)
                    d[vals[0].strip()] = vals[1].strip()
    return d

lines = ['ROLE_ID=25f32932-4c38-500d-e08f-7b75d6919f68\n', 'ROLE_SECRET=70240597-82a2-61eb-6989-83a87af34c0a\n', '#This is a comment\n', '\n', '  ENVIRONMENT = Dev\n', 'S3_SFTP=example.net\n']

print(parse_config("/Users/prajwal.shetty/PycharmProjects/ProblemSolving/Interviews/DeliveryHero/config_file"))