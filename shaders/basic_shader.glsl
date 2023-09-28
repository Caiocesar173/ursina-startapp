// Vertex Shader
void vert() {
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}

// Fragment Shader
void frag() {
    vec4 color = texture2D(texture, gl_TexCoord[0].xy);
    color.rgb = vec3(1.0) - color.rgb;  // Inverte as cores
    gl_FragColor = color;
}
