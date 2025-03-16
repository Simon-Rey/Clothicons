import math
import cairo
import svgwrite


def tshirt_svg(filename, neck_width=20, neck_depth=8, body_width=47, sleeve_angle=30, sleeve_length=10, sleeve_width=15, body_length=70):
    # Fixed canvas size
    canvas_size = 512

    # Convert percentages to absolute values
    neck_width_px = (neck_width / 100) * canvas_size
    neck_depth_px = (neck_depth / 100) * canvas_size
    body_width_px = (body_width / 100) * canvas_size
    sleeve_length_px = (sleeve_length / 100) * canvas_size
    body_length_px = (body_length / 100) * canvas_size

    # Half dimensions for symmetry
    half_body = body_width_px / 2
    sleeve_angle_deg = sleeve_angle
    sleeve_angle = math.radians(sleeve_angle)

    # Bottom corners
    bottom_left = (canvas_size / 2 - half_body, (canvas_size + body_length_px) / 2)
    bottom_right = (canvas_size / 2 + half_body, (canvas_size + body_length_px) / 2)

    sleeve_width_px = (sleeve_width / 100) * canvas_size
    sleeve_gap_px = sleeve_width_px / math.sin(sleeve_angle)

    sleeve_low_endpoint_x_offset = math.sin(sleeve_angle) * sleeve_length_px
    sleeve_low_endpoint_y_offset = math.cos(sleeve_angle) * sleeve_length_px

    sleeve_high_endpoint_x_offset = math.sin(math.radians(90 - sleeve_angle_deg)) * sleeve_width_px
    sleeve_high_endpoint_y_offset = math.cos(math.radians(90 - sleeve_angle_deg)) * sleeve_width_px

    neck_leftover_px = (body_width_px - neck_width_px) / 2

    surface = cairo.SVGSurface(filename, canvas_size, canvas_size)
    ctx = cairo.Context(surface)

    # Set stroke properties
    ctx.set_line_width(5)
    ctx.set_source_rgb(0, 0, 0)  # Black stroke

    # Move to bottom left
    ctx.move_to(*bottom_left)

    # Draw T-shirt path
    ctx.rel_line_to(body_width_px, 0)
    ctx.rel_line_to(0, -body_length_px + sleeve_gap_px)
    ctx.rel_line_to(sleeve_low_endpoint_x_offset, sleeve_low_endpoint_y_offset)
    ctx.rel_line_to(sleeve_high_endpoint_x_offset, -sleeve_high_endpoint_y_offset)
    ctx.rel_line_to(-sleeve_low_endpoint_x_offset - sleeve_high_endpoint_x_offset,
                    -sleeve_low_endpoint_y_offset + sleeve_high_endpoint_y_offset - sleeve_gap_px)
    ctx.rel_line_to(-neck_leftover_px, 0)
    ctx.rel_line_to(-neck_width_px / 2, neck_depth_px)
    ctx.rel_line_to(-neck_width_px / 2, -neck_depth_px)
    ctx.rel_line_to(-neck_leftover_px, 0)
    ctx.rel_line_to(-sleeve_high_endpoint_x_offset - sleeve_low_endpoint_x_offset,
                    -sleeve_high_endpoint_y_offset + sleeve_low_endpoint_y_offset + sleeve_gap_px)
    ctx.rel_line_to(sleeve_high_endpoint_x_offset, sleeve_high_endpoint_y_offset)
    ctx.rel_line_to(sleeve_low_endpoint_x_offset, -sleeve_low_endpoint_y_offset)

    # Close path
    ctx.close_path()

    ctx.fill()

    # Save the SVG file
    surface.finish()


def tanktop_svg(filename):
    dwg = svgwrite.Drawing(filename, size=("24px", "24px"), viewBox="0 0 24 24")
