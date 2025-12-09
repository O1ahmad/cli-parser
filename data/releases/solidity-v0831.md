# Solidity - v0.8.31

**Release Name**: Version 0.8.31
**Published**: 2025-12-03T09:35:58Z
**Repository**: https://github.com/ethereum/solidity

---

We are excited to announce the release of the Solidity Compiler [v0.8.31](https://www.soliditylang.org/blog/2025/12/03/solidity-0.8.31-release-announcement)!

This version of the compiler brings support for the new EVM features introduced by the Fusaka network upgrade, extends the functionality of storage layout specifiers and deprecates the first batch of features scheduled for removal in the 0.9.0 breaking release. We are also adding official ARM Linux builds.

## Changelog

### Language Features:
* Custom Storage Layout: Allow using `constant` state variables in the base slot expression.
* DocString Parser: Warn about deprecation of inline assembly special comment `memory-safe-assembly`.
* Syntax Checker: Warn about deprecation of ABI coder v1.
* Syntax Checker: Warn about deprecation of virtual modifiers.
* Type Checker: Warn about deprecation of `send` and `transfer` functions on instances of `address`.
* Type Checker: Warn about deprecation of comparisons between variables of contract types.
* Yul: Introduce builtin `clz(x)` for counting the number of leading zero bits in a 256-bit word.


### Compiler Features:
* ethdebug: Experimental support for instructions and source locations under EOF.
* EVM: Set default EVM Version to `osaka`.


### Bugfixes:
* Assembler: Fix not using a fixed-width type for IDs being assigned to subassemblies nested more than one level away, resulting in inconsistent `--asm-json` output between target architectures.
* Yul Optimizer: Fix edge case in which invalid Yul code is produced by ExpressionSimplifier due to expressions being substituted that contain out-of-scope variables.


### Build System:
* Enable Linux arm64 binaries for testing and releases.
* Ubuntu PPA Packages: Discontinue the PPA as a binary distribution channel.
* Update minimum version requirements of Boost to 1.83.0 for non-windows builds and of GCC and Clang to 13.3 and 18.1.3, respectively. Fixes infinite recursion on `boost::rational` comparison affecting compiler binaries built with GCC<14.0 and Boost<1.75.

We would especially like to thank all the contributors that made this release possible:
Afounso Souza, Coder, David Klank, Doryu, Emmanuel Ferdman, FT, Fibonacci747, GarmashAlex, Henry Chu, James Niken, Kamil Śliwak, Kendra Karol Sevilla, Martin Blicha, Matheus Aguiar, Michael Cho, MozirDmitriy, Nikola Matić, ParKing666, Patrick Collins, Saw-mon & Natalie, Shane, Tomass, Tronica, clonker, emmmm, fhf, fuder.eth, kilavvy, otc group, phrwlk, r0qs, radik878