import io


def create_mock_file_from_text(text):
    return io.BytesIO(text.encode('utf_8'))


def reset_mock_file_read_pointer_position(mock_file):
    mock_file.seek(0)