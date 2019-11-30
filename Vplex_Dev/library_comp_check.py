from Vplex_Dev.artifactory import ArtifactoryPath
import re

def versionCompare(v1, v2):

    print(f'Comparision between {v1, v2}')
    # Initializer for the version arrays
    i = 0

    # We have taken into consideration that both the
    # versions will contains equal number of delimiters
    while (i < len(v1)):
        try:
            # Version 2 is greater than version 1
            if str(v2[i]) > str(v1[i]):
                return v2

            elif int(v2[i]) > int(v1[i]):
                return v2

            if str(v1[i]) > str(v2[i]):
                return v1
            # Version 1 is greater than version 2
            elif int(v1[i]) > int(v2[i]):
                return v1
        except:
            print("Got exception")
            pass

        # We can't conclude till now
        i += 1

    # Both the versions are equal
    return 0

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
    #     print(str(li))
    optimized_array = []
    maximum = re.findall(r"[\w']+",li[0])
    for i in range(1, len(li)):
        arr = re.findall(r"[\w']+",li[i])
        if arr[0] == maximum[0]:
            maximum = versionCompare(maximum, arr)
            print(f'Current maximum={maximum}')

    for i in range(len(li)):
        arr = re.findall(r"[\w']+",li[i])
        if arr == maximum:
            optimized_array.append(li[i])
    print(f'Optimization {optimized_array}')


check_version_library()