def export_visualization(fig, export_type, file_name):
    if export_type == 'html':
        fig.write_html(file_name)
    elif export_type == 'png':
        fig.write_image(file_name)
    else:
        raise ValueError("Unsupported export type")
