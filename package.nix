{
  python313,
  pyNetworking,
}: let
  python = python313;
  pythonPkgs = python.pkgs;
  inherit (pythonPkgs) buildPythonPackage;
in
  buildPythonPackage (final: {
    pname = "remote-overlay-client";
    version = "0.1";

    src = ./.;

    propagatedBuildInputs = [
      python.pkgs.setuptools
    ];

    dependencies = [
      pyNetworking
    ];

    pyproject = true;
  })
