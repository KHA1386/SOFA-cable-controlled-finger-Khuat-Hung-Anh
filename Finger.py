# -*- coding: utf-8 -*-

import os
from FingerControllerTime import FingerControllerTime

path = os.path.dirname(os.path.abspath(__file__)) + "/mesh/"


def createScene(rootNode):
    # Khai báo các Plugins
    rootNode.addObject("RequiredPlugin", name="SoftRobots")
    rootNode.addObject("RequiredPlugin", name="SofaPython3")
    rootNode.addObject(
        "RequiredPlugin",
        pluginName=[
            "Sofa.Component.AnimationLoop",
            "Sofa.Component.Constraint.Lagrangian.Correction",
            "Sofa.Component.Constraint.Lagrangian.Solver",
            "Sofa.Component.Engine.Select",
            "Sofa.Component.IO.Mesh",
            "Sofa.Component.LinearSolver.Direct",
            "Sofa.Component.Mass",
            "Sofa.Component.ODESolver.Backward",
            "Sofa.Component.Setting",
            "Sofa.Component.SolidMechanics.FEM.Elastic",
            "Sofa.Component.SolidMechanics.Spring",
            "Sofa.Component.Topology.Container.Constant",
            "Sofa.Component.Visual",
            "Sofa.GL.Component.Rendering3D",
        ],
    )
    rootNode.addObject(
        "VisualStyle",
        displayFlags="showVisualModels hideBehaviorModels showCollisionModels hideBoundingCollisionModels hideForceFields showInteractionForceFields hideWireframe",
    )

    # Khởi tạo node chính cho đối tượng ngón tay
    finger = rootNode.addChild("finger")


    # =========================================================================
    # [BƯỚC 1] Khai báo mô hình (Geometry & Topology)
    # =========================================================================
    finger.addObject(
        "MeshVTKLoader", name="loader", filename=path + "finger.vtk"
    )
    finger.addObject("MeshTopology", src="@loader", name="container")
    finger.addObject(
        "MechanicalObject",
        name="tetras",
        template="Vec3",
        showIndices=False,
        showIndicesScale=4e-5,
    )


    # =========================================================================
    # [BƯỚC 2] Khai báo vật liệu và tham số 
    # =========================================================================
    rootNode.gravity = [0, -9810, 0]
    finger.addObject("UniformMass", totalMass=0.075)
    finger.addObject(
        "TetrahedronFEMForceField",
        template="Vec3",
        name="FEM",
        method="large",
        poissonRatio=0.45,
        youngModulus=600,
    )


    # =========================================================================
    # [BƯỚC 3] Thiết lập điều kiện biên 
    # =========================================================================
    finger.addObject(
        "BoxROI", name="roi", box=[-15, 0, 0, 5, 10, 15], drawBoxes=True
    )
    finger.addObject(
        "RestShapeSpringsForceField",
        points=finger.roi.indices.getLinkPath(),
        stiffness=1e12,
    )
    finger.addObject("GenericConstraintCorrection")


    # =========================================================================
    # [BƯỚC 4] Khai báo Actuation hoặc tải ngoài 
    # =========================================================================
    cable = finger.addChild("cable")
    cable.addObject(
        "MechanicalObject",
        position=[
            [-17.5, 12.5, 2.5],
            [-32.5, 12.5, 2.5],
            [-47.5, 12.5, 2.5],
            [-62.5, 12.5, 2.5],
            [-77.5, 12.5, 2.5],
            [-85.5, 12.5, 6.5],
            [-85.5, 12.5, 8.5],
            [-83.5, 12.5, 4.5],
            [-83.5, 12.5, 10.5],
            [-77.5, 12.5, 12.5],
            [-62.5, 12.5, 12.5],
            [-47.5, 12.5, 12.5],
            [-32.5, 12.5, 12.5],
            [-17.5, 12.5, 12.5],
        ],
    )
    cable.addObject(
        "CableConstraint",
        name="aCableActuator",
        indices=list(range(0, 14)),
        minForce=0,
        pullPoint=[0.0, 12.5, 2.5],
    )
    cable.addObject("BarycentricMapping")
    cable.addObject(
        FingerControllerTime(name="FingerControllerTime", node=cable)
    )

    # =========================================================================
    # [BƯỚC 5] Thiết lập Solver 
    # =========================================================================
    # Bộ giải toán cục bộ (cho ngón tay)
    finger.addObject(
        "EulerImplicitSolver",
        name="odesolver",
        rayleighMass=0.1,
        rayleighStiffness=0.1,
    )
    finger.addObject(
        "SparseLDLSolver", template="CompressedRowSparseMatrixMat3x3d"
    )
    # Bộ giải điều kiện ràng buộc toàn cục
    rootNode.addObject(
        "BlockGaussSeidelConstraintSolver", tolerance=1e-5, maxIterations=100
    )

    # =========================================================================
    # [BƯỚC 6] Chạy mô phỏng, thiết lập bước thời gian dt
    # =========================================================================
    rootNode.dt = 0.01
    rootNode.addObject("FreeMotionAnimationLoop")
    rootNode.addObject("DefaultVisualManagerLoop")

    # =========================================================================
    # [BƯỚC 7] Xuất và trực quan hóa kết quả (Visualization)
    # =========================================================================
    fingerVisu = finger.addChild("visu")
    fingerVisu.addObject(
        "MeshSTLLoader", filename=path + "finger.stl", name="loader"
    )
    fingerVisu.addObject("OglModel", src="@loader", color=[0.0, 0.7, 0.7, 1])
    fingerVisu.addObject("BarycentricMapping")

    return rootNode
