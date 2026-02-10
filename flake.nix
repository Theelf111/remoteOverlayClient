{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    inherit (nixpkgs) lib;
    forEachSystem = lib.genAttrs lib.systems.flakeExposed;
    localPkgs = system: nixpkgs.legacyPackages.${system};
  in {
    packages = forEachSystem (system: let
      pkgs = localPkgs system;
    in rec {
      remote-overlay-client =
        pkgs.callPackage ./package.nix {
        };

      default = remote-overlay-client;

      environment = pkgs.python313.withPackages (_: [remote-overlay-client]);
    });
  };
}
