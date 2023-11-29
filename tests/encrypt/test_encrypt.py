import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123, "key")
    with pytest.raises(TypeError):
        encrypt_message("message", "key")

    assert encrypt_message("xablau", 5) == "albax_u"
    assert encrypt_message("todoido", 3) == "dot_odio"

    assert encrypt_message("xablau", 6) == "ualbax"
    assert encrypt_message("todoido", 4) == "odi_odot"
