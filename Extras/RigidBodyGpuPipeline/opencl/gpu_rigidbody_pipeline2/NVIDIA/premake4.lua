	
	hasCL = findOpenCL_NVIDIA()
	
	if (hasCL) then

		project "OpenCL_gpu_rigidbody_pipeline2_NVIDIA"

		initOpenCL_NVIDIA()
	
		language "C++"
				
		kind "ConsoleApp"
		targetdir "../../../bin"

		initOpenGL()
		initGlew()


			includedirs {
		"../../primitives",
		"../../../bullet2"
		}
		
		files {
			"../main.cpp",
			"../CLPhysicsDemo.cpp",
			"../CLPhysicsDemo.h",
			"../GLInstancingRenderer.cpp",
			"../GLInstancingRenderer.h",
			"../GlutRenderer.cpp",
			"../GlutRenderer.h",
			"../Win32OpenGLRenderManager.cpp",
			"../Win32OpenGLRenderManager.h",	
			"../../gpu_rigidbody_pipeline/btConvexUtility.cpp",
			"../../gpu_rigidbody_pipeline/btConvexUtility.h",
			"../../gpu_rigidbody_pipeline/btGpuNarrowPhaseAndSolver.cpp",
			"../../gpu_rigidbody_pipeline/btGpuNarrowPhaseAndSolver.h",
			"../../../dynamics/basic_demo/ConvexHeightFieldShape.cpp",
			"../../../dynamics/basic_demo/ConvexHeightFieldShape.h",
			"../../../bullet2/LinearMath/btConvexHullComputer.cpp",
			"../../../bullet2/LinearMath/btConvexHullComputer.h",
			"../../broadphase_benchmark/findPairsOpenCL.cpp",
			"../../broadphase_benchmark/findPairsOpenCL.h",
			"../../broadphase_benchmark/btGridBroadphaseCL.cpp",
			"../../broadphase_benchmark/btGridBroadphaseCL.h",
			"../../3dGridBroadphase/Shared/bt3dGridBroadphaseOCL.cpp",
			"../../3dGridBroadphase/Shared/bt3dGridBroadphaseOCL.h",
			"../../3dGridBroadphase/Shared/btGpu3DGridBroadphase.cpp",
			"../../3dGridBroadphase/Shared/btGpu3DGridBroadphase.h",
			"../../../bullet2/LinearMath/btAlignedAllocator.cpp",
			"../../../bullet2/LinearMath/btQuickprof.cpp",
			"../../../bullet2/LinearMath/btQuickprof.h",
			"../../../bullet2/BulletCollision/BroadphaseCollision/btBroadphaseProxy.cpp",
			"../../../bullet2/BulletCollision/BroadphaseCollision/btOverlappingPairCache.cpp",
			"../../../bullet2/BulletCollision/BroadphaseCollision/btSimpleBroadphase.cpp",
			"../../basic_initialize/btOpenCLUtils.cpp",
			"../../basic_initialize/btOpenCLUtils.h",
			"../../opengl_interop/btOpenCLGLInteropBuffer.cpp",
			"../../opengl_interop/btOpenCLGLInteropBuffer.h",
			"../../opengl_interop/btStopwatch.cpp",
			"../../opengl_interop/btStopwatch.h"
		}
		
	end
