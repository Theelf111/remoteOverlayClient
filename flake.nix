{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    pyNetworking = {
      url = "github:Theelf111/remoteOverlayClient";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {nixpkgs, pyNetworking, ...}: let
    inherit (nixpkgs) lib;
    forEachSystem = lib.genAttrs lib.systems.flakeExposed;
    localPkgs = system: nixpkgs.legacyPackages.${system};
  in {
    packages = forEachSystem (system: let
      pkgs = localPkgs system;
    in rec {
      remote-overlay-client =
        pkgs.callPackage ./package.nix {
          pyNetworking = pyNetworking.packages.${system}.default;
        };

      default = remote-overlay-client;

      environment = pkgs.python313.withPackages (_: [remote-overlay-client]);
    });
  };
}
