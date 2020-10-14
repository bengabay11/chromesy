import getpass

from chpass import parse_args


def test_default_export():
    mode = "export"
    args = parse_args([mode])
    assert args.mode == mode
    assert not args.all_data
    assert args.user == getpass.getuser()
    assert args.destination_folder == "dist"
    assert args.file_adapter == "csv"
    assert not hasattr(args, "from_file")


def test_default_import():
    mode = "import"
    from_file = "passwords.csv"
    args = parse_args([mode, "-f", from_file])
    assert args.mode == mode
    assert not hasattr(args, "all_data")
    assert args.user == getpass.getuser()
    assert not hasattr(args, "destination_folder")
    assert args.file_adapter == "csv"
    assert args.from_file == from_file


def test_user_flag_export():
    mode = "export"
    user = getpass.getuser()
    args = parse_args(["-u", user, mode])
    assert args.mode == mode
    assert args.user == user


def test_user_flag_import():
    mode = "import"
    from_file = "passwords.csv"
    user = getpass.getuser()
    args = parse_args(["-u", user, mode, "-f", from_file])
    assert args.mode == mode
    assert args.user == user


def test_file_adapter_flag_export():
    mode = "export"
    file_adapter = "json"
    args = parse_args(["-i", file_adapter, mode])
    assert args.mode == mode
    assert args.file_adapter == file_adapter


def test_file_adapter_flag_import():
    mode = "import"
    from_file = "passwords.csv"
    file_adapter = "json"
    args = parse_args(["-i", file_adapter, mode, "-f", from_file])
    assert args.mode == mode
    assert file_adapter == file_adapter


def test_export_all_data_flag():
    mode = "export"
    args = parse_args([mode, "-a"])
    assert args.mode == mode
    assert args.all_data


def test_export_destination_folder_flag():
    mode = "export"
    destination_folder = "dist"
    args = parse_args([mode, "-d", destination_folder])
    assert args.mode == mode
    assert args.destination_folder == destination_folder
