select distinct presupuestoscompras.idPresupuesto,
		proveedores.Nombre,
		presupuestoscompras.FechaPresupuesto,
		usuarios.NombreUSR	
from 
		presupuestoscompras,
		usuarios,
		presupuestoscomprasproductos,
		proveedores	
where
	presupuestoscompras.idProveedor = proveedores.idProveedor and
	presupuestoscompras.idComprador = usuarios.idUsuario 
	order by presupuestoscompras.idPresupuesto
	
	
	
	
select presupuestoscomprasproductos.idPresupuesto,
	productoscomprados.NombreProducto, presupuestoscomprasproductos.cantidad, presupuestoscomprasproductos.precio from
	presupuestoscomprasproductos, productoscomprados
	where presupuestoscomprasproductos.idProducto = productoscomprados.idProducto
	 
	 
