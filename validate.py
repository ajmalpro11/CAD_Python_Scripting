# ============================================================
# RetroPad - Validation Script
# Description : Symmetric difference validation for all parts
# ============================================================

from build123d import *

def validate(generated, stl_path, part_name, tolerance=1.0):
    """
    Validates generated geometry against reference STL
    using symmetric difference method.
    """
    print(f"\n── Validating {part_name} ──")

    # Import reference STL
    importer = Mesher()
    ref_shape = importer.read(stl_path)[0]

    # Align centers
    ref_center = ref_shape.center()
    gen_center = generated.center()
    ref_moved  = ref_shape.moved(Location(gen_center - ref_center))

    # Symmetric difference
    diff_A_minus_B = generated - ref_moved
    diff_B_minus_A = ref_moved - generated

    vol_A_minus_B = diff_A_minus_B.volume if diff_A_minus_B else 0
    vol_B_minus_A = diff_B_minus_A.volume if diff_B_minus_A else 0

    print(f"Reference Volume : {ref_shape.volume:.3f} mm³")
    print(f"Generated Volume : {generated.volume:.3f} mm³")
    print(f"A - B volume     : {vol_A_minus_B:.3f} mm³")
    print(f"B - A volume     : {vol_B_minus_A:.3f} mm³")

    if abs(vol_A_minus_B) < tolerance and abs(vol_B_minus_A) < tolerance:
        print(f"✅ VALIDATION PASSED - {part_name} matches reference!")
    else:
        print(f"❌ VALIDATION FAILED - {part_name} differs!")
        print(f"   Total difference: {abs(vol_A_minus_B) + abs(vol_B_minus_A):.3f} mm³")

# TODO: Import each part and validate
print("Run individual part validations here!")
