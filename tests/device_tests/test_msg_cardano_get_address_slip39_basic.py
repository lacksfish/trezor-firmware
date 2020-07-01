# This file is part of the Trezor project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import pytest

from trezorlib.cardano import PROTOCOL_MAGICS, get_address
from trezorlib.tools import parse_path

from ..common import MNEMONIC_SLIP39_BASIC_20_3of6


@pytest.mark.altcoin
@pytest.mark.cardano
@pytest.mark.skip_t1  # T1 support is not planned
@pytest.mark.skip_ui
@pytest.mark.parametrize(
    "path,protocol_magic,expected_address",
    [
        # mainnet
        (
            "m/44'/1815'/0'/0/0",
            PROTOCOL_MAGICS["mainnet"],
            "Ae2tdPwUPEYxF9NAMNdd3v2LZoMeWp7gCZiDb6bZzFQeeVASzoP7HC4V9s6",
        ),
        (
            "m/44'/1815'/0'/0/1",
            PROTOCOL_MAGICS["mainnet"],
            "Ae2tdPwUPEZ1TjYcvfkWAbiHtGVxv4byEHHZoSyQXjPJ362DifCe1ykgqgy",
        ),
        (
            "m/44'/1815'/0'/0/2",
            PROTOCOL_MAGICS["mainnet"],
            "Ae2tdPwUPEZGXmSbda1kBNfyhRQGRcQxJFdk7mhWZXAGnapyejv2b2U3aRb",
        ),
        # testnet
        # data generated by code under test
        (
            "m/44'/1815'/0'/0/0",
            PROTOCOL_MAGICS["testnet"],
            "2657WMsDfac7SH1rhA2PWBggGAPrKyLt1r9SL9gajPxxcH15ZxuCUb4aK9mQ9w7dU",
        ),
        (
            "m/44'/1815'/0'/0/1",
            PROTOCOL_MAGICS["testnet"],
            "2657WMsDfac6Cmfg4Varph2qyLKGi2K9E8jrtvjHVzfSjmbTMGy5sY3HpxCKsmtDA",
        ),
        (
            "m/44'/1815'/0'/0/2",
            PROTOCOL_MAGICS["testnet"],
            "2657WMsDfac5ANb5Mw6Rbgdz6nvs2Tu675vGbbVSzXQbAkQuMWtqBvEeKTrHNtXY7",
        ),
    ],
)
@pytest.mark.setup_client(mnemonic=MNEMONIC_SLIP39_BASIC_20_3of6, passphrase=True)
def test_cardano_get_address(client, path, protocol_magic, expected_address):
    # enter passphrase
    assert client.features.passphrase_protection is True
    client.use_passphrase("TREZOR")

    address = get_address(client, parse_path(path), protocol_magic)
    assert address == expected_address
