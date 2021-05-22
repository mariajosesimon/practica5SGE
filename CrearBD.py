import pymysql


def CrearTablas():
    db = pymysql.connect(host="127.0.0.1", user="root", db="mibd2", port=3306)
    cursor = db.cursor()
        # phpMyAdmin SQL Dump
    # version 5.1.0
    # https://www.phpmyadmin.net/
    #
    # Servidor: 127.0.0.1
    # Tiempo de generación: 20-05-2021 a las 20:33:11
    # Versión del servidor: 10.4.18-MariaDB
    # Versión de PHP: 8.0.3

    #SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
    #START TRANSACTION;
    #SET time_zone = "+00:00";



    #
    # Base de datos: `mibd2`
    #

    # ############################

    #
    # Estructura de tabla para la tabla `clientes`
    #
    clientes="CREATE TABLE IF NOT EXISTS `clientes` (`idCliente` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY PRIMARY KEY,   `Nombre` varchar(255) NOT NULL,   `Apellidos` varchar(255) NOT NULL,   `Ciudad` varchar(50) NOT NULL,   `Telefono` int(11) DEFAULT NULL,   `NIF` varchar(10) NOT NULL,   `Email` varchar(50) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(clientes)

    # ############################

    #
    # Estructura de tabla para la tabla `departamentos`
    #
    departamentos="CREATE TABLE IF NOT EXISTS `departamentos` (   `idDepartamento` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `NombreDepartamento` varchar(25) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(departamentos)
    #


    #
    # Estructura de tabla para la tabla `facturacomprasproductos`
    #
    facturacomprasproductos="CREATE TABLE IF NOT EXISTS `facturacomprasproductos` (   `idFactura` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `idProducto` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL,   `idConcepto` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(facturacomprasproductos)
    # ############################

    #
    # Estructura de tabla para la tabla `facturascompras`
    #
    facturascompras="CREATE TABLE IF NOT EXISTS `facturascompras` (   `idFactura` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `nFactura` int(11) NOT NULL,   `idProveedor` int(11) NOT NULL,   `FechaFactura` date NOT NULL,   `idComprador` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(facturascompras)
    # ############################

    #
    # Estructura de tabla para la tabla `facturasventas`
    #
    facturasventas="CREATE TABLE IF NOT EXISTS `facturasventas` (   `idFactura` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `nFactura` int(11) NOT NULL,   `idCliente` int(11) NOT NULL,   `FechaFactura` date NOT NULL,   `idVendedor` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(facturasventas)
    # ############################

    #
    # Estructura de tabla para la tabla `facturaventasproductos`
    #
    facturaventasproductos="CREATE TABLE IF NOT EXISTS `facturaventasproductos` (   `idFactura` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `idProducto` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL,   `idConcepto` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"  # ############################
    cursor.execute(facturaventasproductos)
    #
    # Estructura de tabla para la tabla `ordenproduccion`
    #
    ordenproduccion="CREATE TABLE IF NOT EXISTS `ordenproduccion` (   `idOrden` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `idProductoFinal` int(11) NOT NULL,   `FechaOrden` date NOT NULL,   `idProductor` int(11) NOT NULL,   `cantidadProducida` int(11) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(ordenproduccion)
    # ############################

    #
    # Estructura de tabla para la tabla `presupuestoscompras`
    #
    presupuestoscompras="CREATE TABLE IF NOT EXISTS `presupuestoscompras` (   `idPresupuesto` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `idProveedor` int(11) NOT NULL,   `FechaPresupuesto` date NOT NULL,   `idComprador` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(presupuestoscompras)
    # ############################

    #
    # Estructura de tabla para la tabla `presupuestoscomprasproductos`
    #
    presupuestoscomprasproductos="CREATE TABLE IF NOT EXISTS `presupuestoscomprasproductos` (   `idPresupuesto` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `idProducto` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL,   `idConcepto` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(presupuestoscomprasproductos)
    # ############################

    #
    # Estructura de tabla para la tabla `presupuestosventas`
    #
    presupuestosventas="CREATE TABLE IF NOT EXISTS `presupuestosventas` (   `idPresupuesto` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `idCliente` int(11) NOT NULL,   `FechaPresupuesto` date NOT NULL,   `idVendedor` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(presupuestosventas)
    # ############################

    #
    # Estructura de tabla para la tabla `presupuestosventasproductos`
    #
    presupuestosventasproductos="CREATE TABLE IF NOT EXISTS `presupuestosventasproductos` (   `idPresupuesto` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `idProducto` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL,   `idPVP` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(presupuestosventasproductos)
    # ############################

    #
    # Estructura de tabla para la tabla `productoscomprados`
    #

    productoscomprados="CREATE TABLE IF NOT EXISTS `productoscomprados` (   `idProducto` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `NombreProducto` varchar(100) NOT NULL,   `Precio` double NOT NULL,   `Stock` int(11) NOT NULL DEFAULT 0 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(productoscomprados)
    # ############################

    #
    # Estructura de tabla para la tabla `productoscreados`
    #

    productoscreados="CREATE TABLE IF NOT EXISTS `productoscreados` (   `idProducto` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `NombreProducto` varchar(100) NOT NULL,   `Precio` double NOT NULL,   `Stock` int(11) DEFAULT 0 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cursor.execute(productoscreados)
    # ############################

    #
    # Estructura de tabla para la tabla `productosutilizadosproduccion`
    #

    productosutilizadosproduccion="CREATE TABLE IF NOT EXISTS `productosutilizadosproduccion` (   `idProductosUtilizadosOrden` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `idOrden` int(11) NOT NULL,   `idProductoUtilizado` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
    cursor.execute(productosutilizadosproduccion)
    # ############################

    #
    # Estructura de tabla para la tabla `proveedores`
    #

    proveedores="CREATE TABLE IF NOT EXISTS `proveedores` (   `idProveedor` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `Nombre` varchar(255) NOT NULL,   `Ciudad` varchar(50) NOT NULL,   `Telefono` int(11) NOT NULL,   `CIF` varchar(10) NOT NULL,   `Email` varchar(50) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
    cursor.execute(proveedores)
    # ############################

    #
    # Estructura de tabla para la tabla `userlogin`
    #

    userlogin="CREATE TABLE IF NOT EXISTS `userlogin` (   `idUsuario` int(11) NOT NULL DEFAULT 0 ,   `NombreUSR` varchar(50) NOT NULL,   `ApellidosUSR` varchar(100) NOT NULL,   `NIF` varchar(10) NOT NULL,   `FechaAlta` date NOT NULL,   `FechaBaja` date DEFAULT NULL,   `Activo` int(1) NOT NULL,   `idDepartamento` int(11) NOT NULL,   `usuario` varchar(25) NOT NULL,   `password` varchar(25) NOT NULL,   `email` varchar(50) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
    cursor.execute(userlogin)
    # ############################

    #
    # Estructura de tabla para la tabla `usuarios`
    #

    usuarios="CREATE TABLE IF NOT EXISTS `usuarios` (   `idUsuario` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,   `NombreUSR` varchar(50) NOT NULL,   `ApellidosUSR` varchar(100) NOT NULL,   `NIF` varchar(10) NOT NULL,   `FechaAlta` date NOT NULL,   `FechaBaja` date DEFAULT NULL,   `Activo` int(1) NOT NULL,   `idDepartamento` int(11) NOT NULL,   `usuario` varchar(25) NOT NULL,   `password` varchar(25) NOT NULL,   `email` varchar(50) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
    cursor.execute(usuarios)
    #
    # Índices para tablas volcadas
    #

    #

    #
    # Indices de la tabla `facturacomprasproductos`
    #
    facturacomprasproductosIND="ALTER TABLE `facturacomprasproductos`    ADD KEY IF NOT EXISTS `FK_idf_fac` (`idFactura`),   ADD KEY IF NOT EXISTS `FK_idp_pro` (`idProducto`); "
    cursor.execute(facturacomprasproductosIND)
    #
    # Indices de la tabla `facturascompras`
    #
    facturascomprasIND="ALTER TABLE `facturascompras`     ADD KEY IF NOT EXISTS`FK_fco_id` (`idComprador`),   ADD KEY IF NOT EXISTS `FK_fco_pro` (`idProveedor`);"
    cursor.execute(facturascomprasIND)
    #
    # Indices de la tabla `facturasventas`
    #
    facturasventasIND="ALTER TABLE `facturasventas`     ADD KEY IF NOT EXISTS`FK_fve_id` (`idVendedor`),   ADD KEY IF NOT EXISTS `FK_fve_pro` (`idCliente`);"
    cursor.execute(facturasventasIND)
    #
    # Indices de la tabla `facturaventasproductos`
    #
    facturaventasproductosIND="ALTER TABLE `facturaventasproductos`     ADD KEY IF NOT EXISTS `FK_idv_fac` (`idFactura`),   ADD KEY IF NOT EXISTS `FK_idv_pro` (`idProducto`);"
    cursor.execute(facturaventasproductosIND)
    #
    # Indices de la tabla `ordenproduccion`
    #
    ordenproduccionIND="ALTER TABLE `ordenproduccion`     ADD KEY  IF NOT EXISTS  `FK_opr_id` (`idProductor`),   ADD KEY  IF NOT EXISTS `FK_pfi_idp` (`idProductoFinal`);"
    cursor.execute(ordenproduccionIND)
    #
    # Indices de la tabla `presupuestoscompras`
    #
    presupuestoscomprasIND="ALTER TABLE `presupuestoscompras`    ADD KEY IF NOT EXISTS  `FK_pco_idU` (`idComprador`),   ADD KEY  IF NOT EXISTS `FK_pco_pro` (`idProveedor`);"
    cursor.execute(presupuestoscomprasIND)
    #
    # Indices de la tabla `presupuestoscomprasproductos`
    #
    presupuestoscomprasproductosIND="ALTER TABLE `presupuestoscomprasproductos`     ADD KEY  IF NOT EXISTS `FK_idp_pre` (`idPresupuesto`),   ADD KEY  IF NOT EXISTS `FK_idp_prd` (`idProducto`);"
    cursor.execute(presupuestoscomprasproductosIND)
    #
    # Indices de la tabla `presupuestosventas`
    #
    presupuestosventasIND="ALTER TABLE `presupuestosventas`      ADD KEY  IF NOT EXISTS `FK_pve_idU` (`idVendedor`),   ADD KEY  IF NOT EXISTS `FK_pve_pro` (`idCliente`);"
    cursor.execute(presupuestosventasIND)
    #
    # Indices de la tabla `presupuestosventasproductos`
    #
    presupuestosventasproductosIND="ALTER TABLE `presupuestosventasproductos`    ADD KEY IF NOT EXISTS  `FK_pvp_prd` (`idProducto`),   ADD KEY  IF NOT EXISTS `FK_pvp_pre` (`idPresupuesto`);"
    cursor.execute(presupuestosventasproductosIND)
    #

    # Indices de la tabla `productosutilizadosproduccion`
    #
    productosutilizadosproduccionIND="ALTER TABLE `productosutilizadosproduccion`     ADD KEY  IF NOT EXISTS `FK_pup_idO` (`idOrden`),   ADD KEY  IF NOT EXISTS `FK_pup_iPU` (`idProductoUtilizado`);"
    cursor.execute(productosutilizadosproduccionIND)
    #

    #
    # Indices de la tabla `usuarios`
    #
    usuariosMOD="ALTER TABLE `usuarios`      ADD KEY  IF NOT EXISTS `FK_dep_id` (`idDepartamento`);"
    cursor.execute(usuariosMOD)
    #
    # AUTO_INCREMENT de las tablas volcadas
    #

    #

    #
    # Restricciones para tablas volcadas
    #

    #
    # Filtros para la tabla `facturacomprasproductos`
    #
    facturacomprasproductosMOD="ALTER TABLE `facturacomprasproductos`  ADD CONSTRAINT `FK_idf_fac` FOREIGN KEY IF NOT EXISTS  (`idFactura`) REFERENCES `facturascompras` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT  `FK_idp_pro` FOREIGN KEY IF NOT EXISTS (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(facturacomprasproductosMOD)
    #
    # Filtros para la tabla `facturascompras`
    #
    facturascomprasMOD="ALTER TABLE `facturascompras`   ADD CONSTRAINT   `FK_fco_id` FOREIGN KEY IF NOT EXISTS (`idComprador`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT   `FK_fco_pro` FOREIGN KEY IF NOT EXISTS (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(facturascomprasMOD)
    #
    # Filtros para la tabla `facturasventas`
    #
    facturasventasMOD="ALTER TABLE `facturasventas`   ADD CONSTRAINT   `FK_fve_id` FOREIGN KEY IF NOT EXISTS(`idVendedor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_fve_pro` FOREIGN KEY IF NOT EXISTS(`idCliente`) REFERENCES `clientes` (`idCliente`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(facturasventasMOD)
    #
    # Filtros para la tabla `facturaventasproductos`
    #
    facturaventasproductosMOD="ALTER TABLE `facturaventasproductos`   ADD CONSTRAINT  `FK_idv_fac` FOREIGN KEY IF NOT EXISTS(`idFactura`) REFERENCES `facturasventas` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT  `FK_idv_pro` FOREIGN KEY  IF NOT EXISTS(`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `facturaventasproductos_ibfk_1` FOREIGN KEY IF NOT EXISTS(`idFactura`) REFERENCES `facturasventas` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `facturaventasproductos_ibfk_2` FOREIGN KEY IF NOT EXISTS (`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(facturaventasproductosMOD)
    #
    # Filtros para la tabla `ordenproduccion`
    #
    ordenproduccionMOD="ALTER TABLE `ordenproduccion`   ADD CONSTRAINT  `FK_opr_id` FOREIGN KEY IF NOT EXISTS(`idProductor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT  `FK_pfi_idp` FOREIGN KEY  IF NOT EXISTS(`idProductoFinal`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(ordenproduccionMOD)
    #
    # Filtros para la tabla `presupuestoscompras`
    #
    presupuestoscomprasMOD="ALTER TABLE `presupuestoscompras`   ADD CONSTRAINT  `FK_pco_idU` FOREIGN KEY IF NOT EXISTS (`idComprador`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_pco_pro` FOREIGN KEY IF NOT EXISTS(`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(presupuestoscomprasMOD)
    #
    # Filtros para la tabla `presupuestoscomprasproductos`
    #
    presupuestoscomprasproductosMOD="ALTER TABLE `presupuestoscomprasproductos`   ADD CONSTRAINT   `FK_idp_prd` FOREIGN KEY IF NOT EXISTS (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_idp_pre` FOREIGN KEY IF NOT EXISTS (`idPresupuesto`) REFERENCES `presupuestoscompras` (`idPresupuesto`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(presupuestoscomprasproductosMOD)
    #
    # Filtros para la tabla `presupuestosventas`
    #
    presupuestosventasMOD="ALTER TABLE `presupuestosventas`   ADD CONSTRAINT `FK_pve_idU` FOREIGN KEY IF NOT EXISTS (`idVendedor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT   `FK_pve_pro` FOREIGN KEY IF NOT EXISTS(`idCliente`) REFERENCES `clientes` (`idCliente`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(presupuestosventasMOD)
    #
    # Filtros para la tabla `presupuestosventasproductos`
    #
    presupuestosventasproductosMOD="ALTER TABLE `presupuestosventasproductos`   ADD CONSTRAINT `FK_pvp_prd` FOREIGN KEY IF NOT EXISTS (`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT  `FK_pvp_pre` FOREIGN KEY IF NOT EXISTS(`idPresupuesto`) REFERENCES `presupuestosventas` (`idPresupuesto`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(presupuestosventasproductosMOD)

    #
    # Filtros para la tabla `productosutilizadosproduccion`
    #
    productosutilizadosproduccionMOD="ALTER TABLE `productosutilizadosproduccion`   ADD CONSTRAINT `FK_pup_iPU` FOREIGN KEY IF NOT EXISTS(`idProductoUtilizado`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT  `FK_pup_idO` FOREIGN KEY IF NOT EXISTS  (`idOrden`) REFERENCES `ordenproduccion` (`idOrden`) ON DELETE CASCADE ON UPDATE CASCADE; "
    cursor.execute(productosutilizadosproduccionMOD)
    #
    # Filtros para la tabla `usuarios`
    #
    usuariosMOD="ALTER TABLE `usuarios`  ADD CONSTRAINT  `FK_dep_id` FOREIGN KEY IF NOT EXISTS (`idDepartamento`) REFERENCES `departamentos` (`idDepartamento`) ON DELETE CASCADE ON UPDATE CASCADE;"
    cursor.execute(usuariosMOD)


     # Volcado de datos para la tabla `departamentos`
    #
    hayDept = "select count(*) from departamentos"
    cursor.execute(hayDept)
    numero = cursor.fetchone()


    if(numero[0] == 0):
        insertdepartamentos="INSERT INTO `departamentos` (`idDepartamento`, `NombreDepartamento`) VALUES (1, 'RRHH'), (2, 'Compras'), (3, 'Ventas'), (4, 'Produccion');"
        cursor.execute(insertdepartamentos)
    # ############################

    hayUSR= "SELECT count(*) FROM `usuarios` WHERE usuario like 'admin'"
    cursor.execute(hayUSR)
    nAdmin = cursor.fetchone()
    if(nAdmin[0] == 0):
        cursor.execute("insert into usuarios (  `NombreUSR`, `idDepartamento`, `usuario`,`password`) VALUES ('admin', 1, 'admin', '1');")

    db.commit()


