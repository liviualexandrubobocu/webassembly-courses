from manim import *

class AdvancedWASMMemoryScene(Scene):
    def construct(self):
        # Introduction
        title = Title("In-Depth Exploration of WebAssembly Memory", match_underline_width_to_text=True)
        self.play(Write(title))
        self.wait(2)

        # Explaining Linear Memory Concept
        linear_memory_title = Text("Linear Memory", font_size=36)
        linear_memory_description = Text(
            "Continuous, growable array of bytes, accessed via pointers.", 
            font_size=24
        ).next_to(linear_memory_title, DOWN)
        self.play(Write(linear_memory_title))
        self.play(FadeIn(linear_memory_description))
        self.wait(2)
        self.play(FadeOut(linear_memory_title), FadeOut(linear_memory_description))

        # Visualizing Memory Allocation
        memory_grid = VGroup(*[Square() for _ in range(10)]).arrange_in_grid(rows=1)
        self.play(Create(memory_grid))
        self.wait(1)

        # Animating Memory Growth
        growth_text = Text("Memory can grow dynamically", font_size=24).to_edge(DOWN)
        self.play(Write(growth_text))
        additional_blocks = VGroup(*[Square() for _ in range(5)]).arrange_in_grid(rows=1).next_to(memory_grid, RIGHT, buff=0.1)
        self.play(memory_grid.animate.shift(LEFT * 2.5))
        self.play(Create(additional_blocks))
        self.wait(2)
        self.play(FadeOut(growth_text))

        # Memory Segments
        segments_text = Text("Memory Segmentation", font_size=36).to_edge(UP)
        self.play(Write(segments_text))
        segment_highlight = Rectangle(color=RED, height=1, width=3).move_to(memory_grid[4:7])
        self.play(Create(segment_highlight))
        self.wait(2)

        # Pointers and Data Access
        pointer_text = Text("Accessing Data via Pointers", font_size=24).to_edge(DOWN)
        pointer_arrow = Arrow(start=DOWN, end=UP).next_to(pointer_text, UP)
        self.play(Write(pointer_text), GrowArrow(pointer_arrow))
        self.play(pointer_arrow.animate.next_to(memory_grid[5], DOWN))
        self.wait(2)

        # Interaction with JavaScript
        js_interaction_title = Text("Interacting with JavaScript", font_size=36).to_edge(UP)
        self.play(ReplacementTransform(segments_text, js_interaction_title))
        self.play(memory_grid.animate.set_color(YELLOW))
        js_code_example = Text("JavaScript Code Interacting with Memory", font_size=24).to_edge(DOWN)
        self.play(Write(js_code_example))
        self.wait(2)

        # Memory Object
        memory_object_text = Text("The WebAssembly Memory Object", font_size=36).to_edge(UP)
        self.play(ReplacementTransform(js_interaction_title, memory_object_text))
        memory_object_description = Text(
            "A resizable ArrayBuffer that holds the raw bytes of memory accessed by the instance.",
            font_size=24
        ).next_to(memory_object_text, DOWN)
        self.play(Write(memory_object_description))
        self.wait(2)

        # Conclusion
        conclusion_text = Text("This animation provides a glimpse into the complex world of WebAssembly memory management.", font_size=24).to_edge(DOWN)
        self.play(Write(conclusion_text))
        self.wait(3)

        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects])
