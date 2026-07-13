from services.inference_service import infer_image

result = infer_image(
    "/Users/vergil/PycharmProjects/wind_blade_ai/data/examples/叶片壳体鼓包.jpg"
)

print(result)