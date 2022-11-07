import wsl

def test():
    home = wsl.home_unc_path()
    print(f"Out: {home}")
