#version 300 es
precision mediump float;
uniform sampler2D Texture;
in vec2 v_text;

out vec3 f_color;
void main() {
  f_color = texture(Texture,v_text).rgb;
}