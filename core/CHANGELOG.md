# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## 2.3.2 [Unreleased]

_Most likely to be released on August 5th._

### Added
- Soft lock.  [#958]
- Auto lock.  [#1027]
- Dedicated `initialized` field in storage.
- Support EXTERNAL transaction inputs with a SLIP-0019 proof of ownership.  [#1052]
- Support pre-signed EXTERNAL transaction inputs.
- Support multiple change-outputs.  [#1098]
- New option `safety-checks` allows overriding "forbidden key path" errors.  [#1126]

### Changed
- `Features.pin_cached` renamed to `unlocked`.
- Forbid all settings if the device is not yet initialized.  [#1056]
- Rewrite USB codec and Protobuf decoder to be more memory-efficient.  [#1089]

### Deprecated
- Deprecate `overwintered` field in `SignTx` and `TxAck`.

### Removed
- Generated protobuf classes now do not contain deprecated fields.

### Fixed
- Fix cancel icon in PIN dialog.  [#1042]
- Fix repaint bug in QR code rendering.  [#1067]
- Fix QR code overlapping in Monero address.  monero-gui#2960, [#1074]
- Re-introduce ability to spend pre-Overwinter UTXO on Zcash-like coins.  [#1030]

### Security


------------

### Older changelog:

Version 2.3.1 [Jun 2020]
* Refactor Bitcoin signing
* Refactor Keychain into a decorator
* Stream previous tx also for Segwit inputs

Version 2.3.0 [Apr 2020]
* Passphrase redesign
* Cache up to 10 sessions (passphrases)
* SD card protection
* Properly limit passphrase to 50 bytes and not 50 characters
* Monero: add confirmation dialog for unlock_time
* Show xpubs with multisig get_address
* Upgrade MicroPython to 1.12
* Introduce FatFS (version 0.14)
* Support Ed25519 in FIDO2

Version 2.2.0 [Jan 2020]
* Remove unused ButtonRequest.data field
* Rework Recovery persistence internally
* Disallow changing of settings via dry-run recovery
* Add feature to retrieve the next U2F counter
* Fix continuous display blinking with Android in U2F
* U2F UX improvements
* Wipe code
* Add screen for time bounds in Stellar

Version 2.1.8 [Nov 2019]
* Support Tezos 005-BABYLON hardfork
* Show XPUBs in GetAddress for multisig
* Security improvements

Version 2.1.7 [Oct 2019]
* Fix low memory issue

Version 2.1.6 [Oct 2019]
* Refactor Shamir related codebase
* Super Shamir
* FIDO2
* FIDO2 credential management via trezorctl
* BackupType in Features
* Fix storage keys module visbility bug (6ad329) introduced in 2.1.3 (46e4c0) which was breaking fw upgrades

Version 2.1.5 [Sep 2019]
* Fix for sluggish U2F authentication when using Shamir
* Fix UI for Shamir with 33 words
* Fix Wanchain signing
* Binance Coin support
* Introduce Features.Capabilities

Version 2.1.4 [Aug 2019 hotfix]
* Shamir Backup reset device hotfix

Version 2.1.3 [Aug 2019]
* Shamir Backup with Recovery persistence
* Touchscreen freeze fix
* Fix display of non-divisible OMNI amounts

Version 2.1.2 [unreleased]
* Shamir Backup feature preview

Version 2.1.1 [Jun 2019]
* Hotfix for touchscreen freeze
* Don't rotate the screen via swipe gesture
* Set screen rotation via user setting
* More strict path validations
* Display non-zero locktime values
* EOS support
* Monero UI fixes
* Speed and memory optimizations

Version 2.1.0 [Mar 2019]
* Security improvements
* Upgraded to new storage format
* Ripple, Stellar, Cardano and NEM fixes
* New coins: ATS, AXE, FLO, GIN, KMD, NIX,
  PIVX, REOSC, XPM, XSN, ZCL
* New ETH tokens
* Included bootloader 2.0.3

Version 2.0.10 [Dec 2018]
* Fix Monero payment ID computation
* Fix issue with touch screen and flickering
* Add support for OMNI layer: OMNI/MAID/USDT
* Add support for new coins: BTX, CPC, GAME, RVN
* Add support for new Ethereum tokens
* Included bootloader 2.0.2

Version 2.0.9 [Nov 2018]
* Small Monero and Segwit bugfixes

Version 2.0.8 [Oct 2018]
* Monero support
* Cardano support
* Stellar support
* Ripple support
* Tezos support
* Decred support
* Groestlcoin support
* Zencash support
* Zcash sapling hardfork support
* Implemented seedless setup

Version 2.0.7 [Jun 2018]
* Bitcoin Cash cashaddr support
* Zcash Overwinter hardfork support
* NEM support
* Lisk support
* Show warning on home screen if PIN is not set
* Support for new coins:
  Bitcoin Private, Fujicoin, Vertcoin, Viacoin, Zcoin
* Support for new Ethereum networks:
  EOS Classic, Ethereum Social, Ellaism, Callisto, EtherGem, Wanchain
* Support for 500+ new Ethereum tokens

Version 2.0.6 [Mar 2018]
* fix layout for Ethereum transactions
* fix public key generation for SSH and GPG
* add special characters to passphrase keyboard

Version 2.0.5 [Mar 2018]
* first public release

[#958]: https://github.com/trezor/trezor-firmware/issues/958
[#1027]: https://github.com/trezor/trezor-firmware/issues/1027
[#1030]: https://github.com/trezor/trezor-firmware/issues/1030
[#1042]: https://github.com/trezor/trezor-firmware/issues/1042
[#1052]: https://github.com/trezor/trezor-firmware/issues/1052
[#1056]: https://github.com/trezor/trezor-firmware/issues/1056
[#1067]: https://github.com/trezor/trezor-firmware/issues/1067
[#1074]: https://github.com/trezor/trezor-firmware/issues/1074
[#1089]: https://github.com/trezor/trezor-firmware/issues/1089
[#1098]: https://github.com/trezor/trezor-firmware/issues/1098
[#1126]: https://github.com/trezor/trezor-firmware/issues/1126
