import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body['name'] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    response_json = kit_response.json()
    assert kit_response.status_code == 201
    assert response_json['name'] == name


def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


def test1_kit_name_1_character_get_positive_response():
    positive_assert(data.kit_body1)


def test2_kit_name_511_characters_get_positive_response():
    positive_assert(data.kit_body2)


def test3_kit_name_0_characters_get_negative_response():
    negative_assert_symbol(data.kit_body3)


def test4_kit_name_512_characters_get_negative_response():
    negative_assert_symbol(data.kit_body4)


def test5_kit_name_special_characters_get_positive_response():
    positive_assert(data.kit_body5)


def test6_kit_name_space_get_positive_response():
    positive_assert(data.kit_body6)


def test7_kit_name_numbers_string_characters_get_positive_response():
    positive_assert(data.kit_body7)


def test8_kit_name_no_param_get_negative_response():
    negative_assert_symbol(data.kit_body8)


def test9_kit_name_numbers_characters_get_negative_response():
    negative_assert_symbol(data.kit_body9)
