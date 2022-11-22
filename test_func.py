import aws_controller


def test_read_item():
    assert aws_controller.get_itemfrom_id("MIDS001")["Item"]["first_name"] == "Yayun"
