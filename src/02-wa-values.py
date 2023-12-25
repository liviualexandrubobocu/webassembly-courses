from manim import *


class WebAssemblyValues(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        self.intro_section()
        self.hexadecimal_section()
        self.integers_section()
        self.web_assembly_text_format_section()
        self.conclusion_section()

    def intro_section(self):
        # Introductory section
        intro_text = Text("WebAssembly Values and Memory Representation", font_size=40).set_color(WHITE)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

    def hexadecimal_section(self):
        # Explanation of hexadecimal values and memory representation
        title = Text("Hexadecimal Values", font_size=36).set_color(WHITE)
        desc1 = Text("In computing, hexadecimal is a base-16 number system.", font_size=24).next_to(title, DOWN)
        desc2 = Text("It uses symbols 0-9 and A-F.", font_size=24).next_to(desc1, DOWN)
        memory_diagram = self.create_memory_diagram().next_to(desc2, DOWN)

        self.play(FadeIn(title))
        self.play(Write(desc1))
        self.play(Write(desc2))
        self.play(FadeIn(memory_diagram))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(desc1), FadeOut(desc2), FadeOut(memory_diagram))

    def create_memory_diagram(self):
        # Create a visual representation of memory with hexadecimal values
        hex_values = ["0x00", "0x1A", "0xFF"]
        memory_cells = VGroup(*[Square().set_fill(WHITE, opacity=0.5) for _ in hex_values])
        memory_cells.arrange(RIGHT, buff=0.1)
        hex_texts = VGroup(*[Text(value).move_to(cell) for value, cell in zip(hex_values, memory_cells)])
        return VGroup(memory_cells, hex_texts).scale(0.5)

    def integers_section(self):
        # Visual explanation of integers and their representation
        title = Text("Integers in Memory", font_size=36).set_color(WHITE)
        desc = Text("Integers are stored in memory as a sequence of bytes.", font_size=24).next_to(title, DOWN)
        integer_diagram = self.create_integer_diagram().next_to(desc, DOWN)

        self.play(FadeIn(title))
        self.play(Write(desc))
        self.play(FadeIn(integer_diagram))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(desc), FadeOut(integer_diagram))

    def create_integer_diagram(self):
        # Diagram to show how integers are represented in memory
        binary_values = ["01000001", "00101010", "00000001"]
        integer_cells = VGroup(*[Square().set_fill(WHITE, opacity=0.5) for _ in binary_values])
        integer_cells.arrange(RIGHT, buff=0.1)
        binary_texts = VGroup(*[Text(value).move_to(cell) for value, cell in zip(binary_values, integer_cells)])
        return VGroup(integer_cells, binary_texts).scale(0.5)

    def web_assembly_text_format_section(self):
        # Examples in WebAssembly text format
        title = Text("WebAssembly Text Format Examples", font_size=36).set_color(WHITE)
        example1 = Text("i32.const 10 ;; Pushes the 32-bit integer 10", font_size=24).next_to(title, DOWN)
        example2 = Text("i64.const -42 ;; Pushes the 64-bit integer -42", font_size=24).next_to(example1, DOWN)

        self.play(FadeIn(title))
        self.play(Write(example1))
        self.play(Write(example2))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(example1), FadeOut(example2))

    def conclusion_section(self):
        conclusion_text = Text("Understanding memory and value representations is crucial for programming in WebAssembly.", font_size=24).set_color(WHITE)
        self.play(Write(conclusion_text))
        self.wait(2)
        self.play(FadeOut(conclusion_text))

# To run this scene from the command line:
# manim -pql script.py WebAssemblyValuesExplained
