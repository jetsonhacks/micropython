include("$(PORT_DIR)/boards/manifest.py")
freeze("$(MPY_DIR)/drivers/rp2_hid/", "gamepad.py")
freeze("$(MPY_DIR)/lib/micropython-lib/python-stdlib/functools/", "functools.py")

