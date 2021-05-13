-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-05-2021 a las 21:22:35
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mibd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `idCliente` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Apellidos` varchar(255) NOT NULL,
  `Ciudad` varchar(50) NOT NULL,
  `Telefono` int(11) DEFAULT NULL,
  `NIF` varchar(10) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `idDepartamento` int(11) NOT NULL,
  `NombreDepartamento` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturacomprasproductos`
--

CREATE TABLE `facturacomprasproductos` (
  `idFactura` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `idConcepto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturascompras`
--

CREATE TABLE `facturascompras` (
  `idFactura` int(11) NOT NULL,
  `nFactura` int(11) NOT NULL,
  `idProveedor` int(11) NOT NULL,
  `FechaFactura` date NOT NULL,
  `idComprador` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturasventas`
--

CREATE TABLE `facturasventas` (
  `idFactura` int(11) NOT NULL,
  `nFactura` int(11) NOT NULL,
  `idCliente` int(11) NOT NULL,
  `FechaFactura` date NOT NULL,
  `idVendedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturaventasproductos`
--

CREATE TABLE `facturaventasproductos` (
  `idFactura` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `idConcepto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenproduccion`
--

CREATE TABLE `ordenproduccion` (
  `idOrden` int(11) NOT NULL,
  `idProductoFinal` int(11) NOT NULL,
  `FechaOrden` date NOT NULL,
  `idProductor` int(11) NOT NULL,
  `cantidadProducida` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuestoscompras`
--

CREATE TABLE `presupuestoscompras` (
  `idPresupuesto` int(11) NOT NULL,
  `idProveedor` int(11) NOT NULL,
  `FechaPresupuesto` date NOT NULL,
  `idComprador` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuestoscomprasproductos`
--

CREATE TABLE `presupuestoscomprasproductos` (
  `idPresupuesto` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `idConcepto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuestosventas`
--

CREATE TABLE `presupuestosventas` (
  `idPresupuesto` int(11) NOT NULL,
  `idCliente` int(11) NOT NULL,
  `FechaPresupuesto` date NOT NULL,
  `idVendedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuestosventasproductos`
--

CREATE TABLE `presupuestosventasproductos` (
  `idPresupuesto` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `idPVP` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productoscomprados`
--

CREATE TABLE `productoscomprados` (
  `idProducto` int(11) NOT NULL,
  `NombreProducto` varchar(100) NOT NULL,
  `Precio` double NOT NULL,
  `Stock` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productoscreados`
--

CREATE TABLE `productoscreados` (
  `idProducto` int(11) NOT NULL,
  `NombreProducto` varchar(100) NOT NULL,
  `Precio` double NOT NULL,
  `Stock` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productosutilizadosproduccion`
--

CREATE TABLE `productosutilizadosproduccion` (
  `idProductosUtilizadosOrden` int(11) NOT NULL,
  `idOrden` int(11) NOT NULL,
  `idProductoUtilizado` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `idProveedor` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Ciudad` varchar(50) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `CIF` varchar(10) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `userlogin`
--

CREATE TABLE `userlogin` (
  `idUsuario` int(11) NOT NULL DEFAULT 0,
  `NombreUSR` varchar(50) NOT NULL,
  `ApellidosUSR` varchar(100) NOT NULL,
  `NIF` varchar(10) NOT NULL,
  `FechaAlta` date NOT NULL,
  `FechaBaja` date DEFAULT NULL,
  `Activo` int(1) NOT NULL,
  `idDepartamento` int(11) NOT NULL,
  `usuario` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `NombreUSR` varchar(50) NOT NULL,
  `ApellidosUSR` varchar(100) NOT NULL,
  `NIF` varchar(10) NOT NULL,
  `FechaAlta` date NOT NULL,
  `FechaBaja` date DEFAULT NULL,
  `Activo` int(1) NOT NULL,
  `idDepartamento` int(11) NOT NULL,
  `usuario` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`idCliente`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`idDepartamento`);

--
-- Indices de la tabla `facturacomprasproductos`
--
ALTER TABLE `facturacomprasproductos`
  ADD PRIMARY KEY (`idConcepto`),
  ADD KEY `FK_idf_fac` (`idFactura`),
  ADD KEY `FK_idp_pro` (`idProducto`);

--
-- Indices de la tabla `facturascompras`
--
ALTER TABLE `facturascompras`
  ADD PRIMARY KEY (`idFactura`),
  ADD KEY `FK_fco_id` (`idComprador`),
  ADD KEY `FK_fco_pro` (`idProveedor`);

--
-- Indices de la tabla `facturasventas`
--
ALTER TABLE `facturasventas`
  ADD PRIMARY KEY (`idFactura`),
  ADD KEY `FK_fve_id` (`idVendedor`),
  ADD KEY `FK_fve_pro` (`idCliente`);

--
-- Indices de la tabla `facturaventasproductos`
--
ALTER TABLE `facturaventasproductos`
  ADD PRIMARY KEY (`idConcepto`),
  ADD KEY `FK_idv_fac` (`idFactura`),
  ADD KEY `FK_idv_pro` (`idProducto`);

--
-- Indices de la tabla `ordenproduccion`
--
ALTER TABLE `ordenproduccion`
  ADD PRIMARY KEY (`idOrden`),
  ADD KEY `FK_opr_id` (`idProductor`),
  ADD KEY `FK_pfi_idp` (`idProductoFinal`);

--
-- Indices de la tabla `presupuestoscompras`
--
ALTER TABLE `presupuestoscompras`
  ADD PRIMARY KEY (`idPresupuesto`) USING BTREE,
  ADD KEY `FK_pco_idU` (`idComprador`),
  ADD KEY `FK_pco_pro` (`idProveedor`);

--
-- Indices de la tabla `presupuestoscomprasproductos`
--
ALTER TABLE `presupuestoscomprasproductos`
  ADD PRIMARY KEY (`idConcepto`),
  ADD KEY `FK_idp_pre` (`idPresupuesto`),
  ADD KEY `FK_idp_prd` (`idProducto`);

--
-- Indices de la tabla `presupuestosventas`
--
ALTER TABLE `presupuestosventas`
  ADD PRIMARY KEY (`idPresupuesto`),
  ADD KEY `FK_pve_idU` (`idVendedor`),
  ADD KEY `FK_pve_pro` (`idCliente`);

--
-- Indices de la tabla `presupuestosventasproductos`
--
ALTER TABLE `presupuestosventasproductos`
  ADD PRIMARY KEY (`idPVP`),
  ADD KEY `FK_pvp_prd` (`idProducto`),
  ADD KEY `FK_pvp_pre` (`idPresupuesto`);

--
-- Indices de la tabla `productoscomprados`
--
ALTER TABLE `productoscomprados`
  ADD PRIMARY KEY (`idProducto`);

--
-- Indices de la tabla `productoscreados`
--
ALTER TABLE `productoscreados`
  ADD PRIMARY KEY (`idProducto`);

--
-- Indices de la tabla `productosutilizadosproduccion`
--
ALTER TABLE `productosutilizadosproduccion`
  ADD PRIMARY KEY (`idProductosUtilizadosOrden`),
  ADD KEY `FK_pup_idO` (`idOrden`),
  ADD KEY `FK_pup_iPU` (`idProductoUtilizado`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`idProveedor`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`),
  ADD KEY `FK_dep_id` (`idDepartamento`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `idCliente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `idDepartamento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `facturacomprasproductos`
--
ALTER TABLE `facturacomprasproductos`
  MODIFY `idConcepto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `facturascompras`
--
ALTER TABLE `facturascompras`
  MODIFY `idFactura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `facturasventas`
--
ALTER TABLE `facturasventas`
  MODIFY `idFactura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `facturaventasproductos`
--
ALTER TABLE `facturaventasproductos`
  MODIFY `idConcepto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ordenproduccion`
--
ALTER TABLE `ordenproduccion`
  MODIFY `idOrden` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `presupuestoscompras`
--
ALTER TABLE `presupuestoscompras`
  MODIFY `idPresupuesto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `presupuestoscomprasproductos`
--
ALTER TABLE `presupuestoscomprasproductos`
  MODIFY `idConcepto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `presupuestosventas`
--
ALTER TABLE `presupuestosventas`
  MODIFY `idPresupuesto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `presupuestosventasproductos`
--
ALTER TABLE `presupuestosventasproductos`
  MODIFY `idPVP` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productoscomprados`
--
ALTER TABLE `productoscomprados`
  MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productoscreados`
--
ALTER TABLE `productoscreados`
  MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productosutilizadosproduccion`
--
ALTER TABLE `productosutilizadosproduccion`
  MODIFY `idProductosUtilizadosOrden` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `idProveedor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `facturacomprasproductos`
--
ALTER TABLE `facturacomprasproductos`
  ADD CONSTRAINT `FK_idf_fac` FOREIGN KEY (`idFactura`) REFERENCES `facturascompras` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_idp_pro` FOREIGN KEY (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `facturascompras`
--
ALTER TABLE `facturascompras`
  ADD CONSTRAINT `FK_fco_id` FOREIGN KEY (`idComprador`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_fco_pro` FOREIGN KEY (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `facturasventas`
--
ALTER TABLE `facturasventas`
  ADD CONSTRAINT `FK_fve_id` FOREIGN KEY (`idVendedor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_fve_pro` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `facturaventasproductos`
--
ALTER TABLE `facturaventasproductos`
  ADD CONSTRAINT `FK_idv_fac` FOREIGN KEY (`idFactura`) REFERENCES `facturasventas` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_idv_pro` FOREIGN KEY (`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `facturaventasproductos_ibfk_1` FOREIGN KEY (`idFactura`) REFERENCES `facturasventas` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `facturaventasproductos_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `ordenproduccion`
--
ALTER TABLE `ordenproduccion`
  ADD CONSTRAINT `FK_opr_id` FOREIGN KEY (`idProductor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_pfi_idp` FOREIGN KEY (`idProductoFinal`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `presupuestoscompras`
--
ALTER TABLE `presupuestoscompras`
  ADD CONSTRAINT `FK_pco_idU` FOREIGN KEY (`idComprador`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_pco_pro` FOREIGN KEY (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `presupuestoscomprasproductos`
--
ALTER TABLE `presupuestoscomprasproductos`
  ADD CONSTRAINT `FK_idp_prd` FOREIGN KEY (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_idp_pre` FOREIGN KEY (`idPresupuesto`) REFERENCES `presupuestoscompras` (`idPresupuesto`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `presupuestosventas`
--
ALTER TABLE `presupuestosventas`
  ADD CONSTRAINT `FK_pve_idU` FOREIGN KEY (`idVendedor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_pve_pro` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `presupuestosventasproductos`
--
ALTER TABLE `presupuestosventasproductos`
  ADD CONSTRAINT `FK_pvp_prd` FOREIGN KEY (`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_pvp_pre` FOREIGN KEY (`idPresupuesto`) REFERENCES `presupuestosventas` (`idPresupuesto`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `productosutilizadosproduccion`
--
ALTER TABLE `productosutilizadosproduccion`
  ADD CONSTRAINT `FK_pup_iPU` FOREIGN KEY (`idProductoUtilizado`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_pup_idO` FOREIGN KEY (`idOrden`) REFERENCES `ordenproduccion` (`idOrden`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `FK_dep_id` FOREIGN KEY (`idDepartamento`) REFERENCES `departamentos` (`idDepartamento`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
