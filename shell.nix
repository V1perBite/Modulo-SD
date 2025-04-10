{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell rec {
  buildInputs = [
    pkgs.python310Full           # Python 3.10
    pkgs.python310Packages.pip   # pip para gestionar las dependencias
  ];

  shellHook = ''
    export PYTHONPATH=$PYTHONPATH:${toString pkgs.python310.sitePackages}
  '';
}
