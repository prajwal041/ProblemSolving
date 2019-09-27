from Vplex_Dev.artifactory import ArtifactoryPath
import re
def check_version_library():
    path = ArtifactoryPath("http://repo.jfrog.org/artifactory/gradle-ivy-local")
    # walking directory tree
    # print(path)
    '''
    Convert each ArtifactoryPath to str
    '''
    li = ['MozillaFirefox-60.7.0esr-78.40.2.x86_64.rpm',
          'MozillaFirefox-60.7.0esr_60.8.0esr-78.40.2_78.43.2.x86_64.drpm',
          'MozillaFirefox-60.8.0esr-78.43.2.x86_64.rpm',
          'MozillaFirefox-60.8.0esr_60.9.0esr-78.43.2_78.46.2.x86_64.drpm',
          'MozillaFirefox-60.9.0esr-78.46.2.x86_64.rpm']
    # for p in path:
    #     li.append(p)
    #     print(li)
    for i in li:
        print(i.split('-'))


def versionCompare(v1, v2):
    # This will split both the versions by '.'
    arr1 = v1.split(".")
    arr2 = v2.split(".")

    # Initializer for the version arrays
    i = 0

    # We have taken into consideration that both the
    # versions will contains equal number of delimiters
    while (i < len(arr1)):

        # Version 2 is greater than version 1
        if int(arr2[i]) > int(arr1[i]):
            return -1

        # Version 1 is greater than version 2
        if int(arr1[i]) > int(arr2[i]):
            return 1

        # We can't conclude till now
        i += 1

    # Both the versions are equal
    return 0
version1 = "1.0.3"
version2 = "1.0.7"
check_version_library()