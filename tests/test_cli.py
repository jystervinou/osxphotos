import pytest
from click.testing import CliRunner

CLI_PHOTOS_DB = "tests/Test-10.15.1.photoslibrary"
LIVE_PHOTOS_DB = "tests/Test-Cloud-10.15.1.photoslibrary/database/photos.db"
RAW_PHOTOS_DB = "tests/Test-RAW-10.15.1.photoslibrary"
PLACES_PHOTOS_DB = "tests/Test-Places-Catalina-10_15_1.photoslibrary"
PLACES_PHOTOS_DB_13 = "tests/Test-Places-High-Sierra-10.13.6.photoslibrary"

CLI_OUTPUT_NO_SUBCOMMAND = [
    "Options:",
    "--db <Photos database path>  Specify Photos database path. Path to Photos",
    "library/database can be specified using either",
    "--db or directly as PHOTOS_LIBRARY positional",
    "argument.",
    "--json                       Print output in JSON format.",
    "-v, --version                Show the version and exit.",
    "-h, --help                   Show this message and exit.",
    "Commands:",
    "  albums    Print out albums found in the Photos library.",
    "  dump      Print list of all photos & associated info from the Photos",
    "  export    Export photos from the Photos database.",
    "  help      Print help; for help on commands: help <command>.",
    "  info      Print out descriptive info of the Photos library database.",
    "  keywords  Print out keywords found in the Photos library.",
    "  list      Print list of Photos libraries found on the system.",
    "  persons   Print out persons (faces) found in the Photos library.",
    "  places    Print out places found in the Photos library.",
    "  query     Query the Photos database using 1 or more search options; if",
]

CLI_OUTPUT_QUERY_UUID = '[{"uuid": "D79B8D77-BFFC-460B-9312-034F2877D35B", "filename": "D79B8D77-BFFC-460B-9312-034F2877D35B.jpeg", "original_filename": "Pumkins2.jpg", "date": "2018-09-28T16:07:07-04:00", "description": "Girl holding pumpkin", "title": "I found one!", "keywords": ["Kids"], "albums": ["Pumpkin Farm", "Test Album", "Multi Keyword"], "persons": ["Katie"], "path": "/tests/Test-10.15.1.photoslibrary/originals/D/D79B8D77-BFFC-460B-9312-034F2877D35B.jpeg", "ismissing": false, "hasadjustments": false, "external_edit": false, "favorite": false, "hidden": false, "latitude": null, "longitude": null, "path_edited": null, "shared": false, "isphoto": true, "ismovie": false, "uti": "public.jpeg", "burst": false, "live_photo": false, "path_live_photo": null, "iscloudasset": false, "incloud": null}]'

CLI_EXPORT_FILENAMES = [
    "Pumkins1.jpg",
    "Pumkins2.jpg",
    "Pumpkins3.jpg",
    "St James Park.jpg",
    "St James Park_edited.jpeg",
    "Tulips.jpg",
    "wedding.jpg",
    "wedding_edited.jpeg",
]

CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES1 = [
    "2019/April/wedding.jpg",
    "2019/July/Tulips.jpg",
    "2018/October/St James Park.jpg",
    "2018/September/Pumpkins3.jpg",
    "2018/September/Pumkins2.jpg",
    "2018/September/Pumkins1.jpg",
]

CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES_ALBUM1 = [
    "Multi Keyword/wedding.jpg",
    "_/Tulips.jpg",
    "_/St James Park.jpg",
    "Pumpkin Farm/Pumpkins3.jpg",
    "Pumpkin Farm/Pumkins2.jpg",
    "Pumpkin Farm/Pumkins1.jpg",
    "Test Album/Pumkins1.jpg",
]

CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES_ALBUM2 = [
    "Multi Keyword/wedding.jpg",
    "NOALBUM/Tulips.jpg",
    "NOALBUM/St James Park.jpg",
    "Pumpkin Farm/Pumpkins3.jpg",
    "Pumpkin Farm/Pumkins2.jpg",
    "Pumpkin Farm/Pumkins1.jpg",
    "Test Album/Pumkins1.jpg",
]

CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES2 = [
    "St James's Park, Great Britain, Westminster, England, United Kingdom/St James Park.jpg",
    "_/Pumpkins3.jpg",
    "_/Pumkins2.jpg",
    "_/Pumkins1.jpg",
    "_/Tulips.jpg",
    "_/wedding.jpg",
]

CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES3 = [
    "2019/{foo}/wedding.jpg",
    "2019/{foo}/Tulips.jpg",
    "2018/{foo}/St James Park.jpg",
    "2018/{foo}/Pumpkins3.jpg",
    "2018/{foo}/Pumkins2.jpg",
    "2018/{foo}/Pumkins1.jpg",
]

CLI_EXPORT_UUID = "D79B8D77-BFFC-460B-9312-034F2877D35B"

CLI_EXPORT_SIDECAR_FILENAMES = ["Pumkins2.jpg", "Pumkins2.json", "Pumkins2.xmp"]

CLI_EXPORT_LIVE = [
    "51F2BEF7-431A-4D31-8AC1-3284A57826AE.jpeg",
    "51F2BEF7-431A-4D31-8AC1-3284A57826AE.mov",
]

CLI_EXPORT_LIVE_ORIGINAL = ["IMG_0728.JPG", "IMG_0728.mov"]

CLI_EXPORT_RAW = ["441DFE2A-A69B-4C79-A69B-3F51D1B9B29C.cr2"]
CLI_EXPORT_RAW_ORIGINAL = ["IMG_0476_2.CR2"]
CLI_EXPORT_RAW_EDITED = [
    "441DFE2A-A69B-4C79-A69B-3F51D1B9B29C.cr2",
    "441DFE2A-A69B-4C79-A69B-3F51D1B9B29C_edited.jpeg",
]
CLI_EXPORT_RAW_EDITED_ORIGINAL = ["IMG_0476_2.CR2", "IMG_0476_2_edited.jpeg"]

CLI_PLACES_JSON = """{"places": {"_UNKNOWN_": 1, "Maui, Wailea, Hawai'i, United States": 1, "Washington, District of Columbia, United States": 1}}"""


def test_osxphotos():
    import osxphotos
    from osxphotos.__main__ import cli

    runner = CliRunner()
    result = runner.invoke(cli, [])
    output = result.output
    assert result.exit_code == 0
    for line in CLI_OUTPUT_NO_SUBCOMMAND:
        assert line in output


def test_osxphotos_help_1():
    # test help command no topic
    import osxphotos
    from osxphotos.__main__ import cli

    runner = CliRunner()
    result = runner.invoke(cli, ["help"])
    output = result.output
    assert result.exit_code == 0
    for line in CLI_OUTPUT_NO_SUBCOMMAND:
        assert line in output


def test_osxphotos_help_2():
    # test help command valid topic
    import osxphotos
    from osxphotos.__main__ import cli

    runner = CliRunner()
    result = runner.invoke(cli, ["help", "persons"])
    output = result.output
    assert result.exit_code == 0
    assert "Print out persons (faces) found in the Photos library." in result.output


def test_osxphotos_help_3():
    # test help command invalid topic
    import osxphotos
    from osxphotos.__main__ import cli

    runner = CliRunner()
    result = runner.invoke(cli, ["help", "foo"])
    output = result.output
    assert result.exit_code == 0
    assert "Invalid command: foo" in result.output


def test_query_uuid():
    import json
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import query

    runner = CliRunner()
    cwd = os.getcwd()
    result = runner.invoke(
        query,
        [
            "--json",
            "--db",
            os.path.join(cwd, CLI_PHOTOS_DB),
            # "./tests/Test-10.15.1.photoslibrary",
            "--uuid",
            "D79B8D77-BFFC-460B-9312-034F2877D35B",
        ],
    )
    assert result.exit_code == 0

    json_expected = json.loads(CLI_OUTPUT_QUERY_UUID)[0]
    json_got = json.loads(result.output)[0]

    assert list(json_expected.keys()).sort() == list(json_got.keys()).sort()

    # check values expected vs got
    # path needs special handling as path is set to full path which will differ system to system
    for key_ in json_expected:
        assert key_ in json_got
        if key_ != "path":
            assert json_expected[key_] == json_got[key_]
        else:
            assert json_expected[key_] in json_got[key_]


def test_export():
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export,
            [
                os.path.join(cwd, CLI_PHOTOS_DB),
                ".",
                "--original-name",
                "--export-edited",
                "-V",
            ],
        )
        assert result.exit_code == 0
        files = glob.glob("*")
        assert sorted(files) == sorted(CLI_EXPORT_FILENAMES)


def test_query_date():
    import json
    import osxphotos
    import os
    import os.path
    from osxphotos.__main__ import query

    runner = CliRunner()
    cwd = os.getcwd()
    result = runner.invoke(
        query,
        [
            "--json",
            "--db",
            os.path.join(cwd, CLI_PHOTOS_DB),
            "--from-date=2018-09-28",
            "--to-date=2018-09-28T23:00:00",
        ],
    )
    assert result.exit_code == 0
    import logging

    logging.warning(result.output)

    json_got = json.loads(result.output)
    assert len(json_got) == 4


def test_export_sidecar():
    import glob
    import os
    import os.path
    import osxphotos

    from osxphotos.__main__ import cli

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            [
                "export",
                "--db",
                os.path.join(cwd, CLI_PHOTOS_DB),
                ".",
                "--original-name",
                "--sidecar=json",
                "--sidecar=xmp",
                f"--uuid={CLI_EXPORT_UUID}",
                "-V",
            ],
        )
        files = glob.glob("*.*")
        assert sorted(files) == sorted(CLI_EXPORT_SIDECAR_FILENAMES)


def test_export_live():
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export,
            [
                os.path.join(cwd, LIVE_PHOTOS_DB),
                ".",
                "--live",
                "--original-name",
                "--export-live",
                "-V",
            ],
        )
        files = glob.glob("*")
        assert sorted(files) == sorted(CLI_EXPORT_LIVE_ORIGINAL)


def test_export_raw():
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(export, [os.path.join(cwd, RAW_PHOTOS_DB), ".", "-V"])
        files = glob.glob("*")
        assert sorted(files) == sorted(CLI_EXPORT_RAW)


def test_export_raw_original():
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export, [os.path.join(cwd, RAW_PHOTOS_DB), ".", "--original-name", "-V"]
        )
        files = glob.glob("*")
        assert sorted(files) == sorted(CLI_EXPORT_RAW_ORIGINAL)


def test_export_raw_edited():
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export, [os.path.join(cwd, RAW_PHOTOS_DB), ".", "--export-edited", "-V"]
        )
        files = glob.glob("*")
        assert sorted(files) == sorted(CLI_EXPORT_RAW_EDITED)


def test_export_raw_edited_original():
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export,
            [
                os.path.join(cwd, RAW_PHOTOS_DB),
                ".",
                "--export-edited",
                "--original-name",
                "-V",
            ],
        )
        files = glob.glob("*")
        assert sorted(files) == sorted(CLI_EXPORT_RAW_EDITED_ORIGINAL)


def test_export_directory_template_1():
    # test export using directory template
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export,
            [
                os.path.join(cwd, CLI_PHOTOS_DB),
                ".",
                "--original-name",
                "-V",
                "--directory",
                "{created.year}/{created.month}",
            ],
        )
        assert result.exit_code == 0
        workdir = os.getcwd()
        for filepath in CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES1:
            assert os.path.isfile(os.path.join(workdir, filepath))


def test_export_directory_template_2():
    # test export using directory template with missing substitution value
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export,
            [
                os.path.join(cwd, CLI_PHOTOS_DB),
                ".",
                "--original-name",
                "-V",
                "--directory",
                "{place.name}",
            ],
        )
        assert result.exit_code == 0
        workdir = os.getcwd()
        for filepath in CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES2:
            assert os.path.isfile(os.path.join(workdir, filepath))


def test_export_directory_template_3():
    # test export using directory template with unmatched substituion value
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export,
            [
                os.path.join(cwd, CLI_PHOTOS_DB),
                ".",
                "--original-name",
                "-V",
                "--directory",
                "{created.year}/{foo}",
            ],
        )
        assert result.exit_code == 2
        assert "Error: Invalid substitution in template" in result.output


def test_export_directory_template_album_1():
    # test export using directory template with multiple albums
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export,
            [
                os.path.join(cwd, CLI_PHOTOS_DB),
                ".",
                "--original-name",
                "-V",
                "--directory",
                "{album}",
            ],
        )
        assert result.exit_code == 0
        workdir = os.getcwd()
        for filepath in CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES_ALBUM1:
            assert os.path.isfile(os.path.join(workdir, filepath))


def test_export_directory_template_album_2():
    # test export using directory template with multiple albums
    # specify default value
    import glob
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import export

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            export,
            [
                os.path.join(cwd, CLI_PHOTOS_DB),
                ".",
                "--original-name",
                "-V",
                "--directory",
                "{album,NOALBUM}",
            ],
        )
        assert result.exit_code == 0
        workdir = os.getcwd()
        for filepath in CLI_EXPORTED_DIRECTORY_TEMPLATE_FILENAMES_ALBUM2:
            assert os.path.isfile(os.path.join(workdir, filepath))


def test_places():
    import json
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import places

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(places, [os.path.join(cwd, PLACES_PHOTOS_DB), "--json"])
        assert result.exit_code == 0
        json_got = json.loads(result.output)
        assert json_got == json.loads(CLI_PLACES_JSON)


def test_place_13():
    # test --place on 10.13
    import json
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import query

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            query,
            [os.path.join(cwd, PLACES_PHOTOS_DB_13), "--json", "--place", "Adelaide"],
        )
        assert result.exit_code == 0
        json_got = json.loads(result.output)

        assert len(json_got) == 1  # single element
        assert json_got[0]["uuid"] == "2L6X2hv3ROWRSCU3WRRAGQ"


def test_no_place_13():
    # test --no-place on 10.13
    import json
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import query

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            query, [os.path.join(cwd, PLACES_PHOTOS_DB_13), "--json", "--no-place"]
        )
        assert result.exit_code == 0
        json_got = json.loads(result.output)

        assert len(json_got) == 1  # single element
        assert json_got[0]["uuid"] == "pERZk5T1Sb+XcKDFRCsGpA"


def test_place_15_1():
    # test --place on 10.15
    import json
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import query

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            query,
            [os.path.join(cwd, PLACES_PHOTOS_DB), "--json", "--place", "Washington"],
        )
        assert result.exit_code == 0
        json_got = json.loads(result.output)

        assert len(json_got) == 1  # single element
        assert json_got[0]["uuid"] == "128FB4C6-0B16-4E7D-9108-FB2E90DA1546"


def test_place_15_2():
    # test --place on 10.15
    import json
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import query

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            query,
            [os.path.join(cwd, PLACES_PHOTOS_DB), "--json", "--place", "United States"],
        )
        assert result.exit_code == 0
        json_got = json.loads(result.output)

        assert len(json_got) == 2  # single element
        uuid = [json_got[x]["uuid"] for x in (0, 1)]
        assert "128FB4C6-0B16-4E7D-9108-FB2E90DA1546" in uuid
        assert "FF7AFE2C-49B0-4C9B-B0D7-7E1F8B8F2F0C" in uuid


def test_no_place_15():
    # test --no-place on 10.15
    import json
    import os
    import os.path
    import osxphotos
    from osxphotos.__main__ import query

    runner = CliRunner()
    cwd = os.getcwd()
    # pylint: disable=not-context-manager
    with runner.isolated_filesystem():
        result = runner.invoke(
            query, [os.path.join(cwd, PLACES_PHOTOS_DB), "--json", "--no-place"]
        )
        assert result.exit_code == 0
        json_got = json.loads(result.output)

        assert len(json_got) == 1  # single element
        assert json_got[0]["uuid"] == "A9B73E13-A6F2-4915-8D67-7213B39BAE9F"
