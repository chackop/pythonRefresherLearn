def zip_archive(source_dir, extension_lists, output_filename):
    """
    Create a zip archive from the specified source directory.

    :param source_dir: The directory to be zipped.
    :param extension_lists: A list of file extensions to include in the zip.
    :param output_filename: The name of the output zip file.
    """
    import os
    from zipfile import ZipFile

    with ZipFile(output_filename, "w") as zipf:
        for root, _, files in os.walk(source_dir):
            rel_path = os.path.relpath(root, source_dir)
            for file in files:
                _, ext = os.path.splitext(file)

                if ext.lower() in extension_lists:
                    zipf.write(
                        os.path.join(root, file), arcname=os.path.join(rel_path, file)
                    )
