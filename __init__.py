# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AdminZoneKorea
                                 A QGIS plugin
 Provide Admin Zone of Korea
                             -------------------
        begin                : 2015-07-06
        copyright            : (C) 2015 by BJ Jang
        email                : jangbi882@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AdminZoneKorea class from file AdminZoneKorea.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .admin_zone_korea import AdminZoneKorea
    return AdminZoneKorea(iface)
