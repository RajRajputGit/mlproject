from setuptools import setup, find_packages


HYPEN_E_DASH = "-e ." 
def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Clean up the new line characters (\n)
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Pro Tip: Ignore the '-e .' used for local installations
        if HYPEN_E_DASH in requirements:
            requirements.remove(HYPEN_E_DASH)
            
    return requirements



setup(
    name="ml-project",
    version="0.1.0",
    author="Braj Rajput",
    # This is where the magic happens:
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
    