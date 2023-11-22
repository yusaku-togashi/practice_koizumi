<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'local' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'root' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';


/* Add any custom values between this line and the "stop editing" line. */



/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
if ( ! defined( 'WP_DEBUG' ) ) {
	define( 'WP_DEBUG', false );
}


define('AUTH_KEY',         '323Ybv35zzayjZ7L9LUPViro+kyAmN8QSMGXbapV+SmH08bTPzjtAFPROhJ88FRZwbJNvi8mjQmPLGE6f4Dthw==');
define('SECURE_AUTH_KEY',  'clzqhdMyrIz7MRA5k2jJaVNlq6VW0eDGC15GFgJO9y96L7fvVV/06CbSdP/h/+G6DjOu6VB4jgoiyClpisBOEQ==');
define('LOGGED_IN_KEY',    'q9gurzVT8r2AZkkFi85Tg6dTEm7WR1Ywz6dira/QZqDw3wd5dKoCXsjG8UgECXYtEQG/YEUJYWx/AT+5++v0Mw==');
define('NONCE_KEY',        'V4iPXRIbFssRvwyZj0jnZpPqbZBn0Yxxcv4jZrq3pT9j9SB27kO9oIvoWJbp/WYspoEGQjdUqxh7orWGBPGs7w==');
define('AUTH_SALT',        '1ScHOAJ28V0PFoXmHJfdqnFjtRkLJOjRPIr5gCCe32n49qFXfisn//N7vOPTCuSNaSLrEgvagi2u/5irMm6tUQ==');
define('SECURE_AUTH_SALT', 'vsP7yTUgGuz5MEdrjjhhQZEpHVB+MsLbiCGJLV2HZ4ZxoIa1xjrHwA32Lxi0FsgRskjAJhfnNvht7kR76iXZ9A==');
define('LOGGED_IN_SALT',   '8wZlhDqHUF6cqE1lJ9Xd7n2VM+z4UlV4RHnaXwgi/yno99JYWTnM0O2LlPPoGMVH77W0eUDf3+BnEanCAL8yBQ==');
define('NONCE_SALT',       '0nD1xfr053hZU4S1nnlzrl26b9bo++xBjzRvdBDOT3zsry7bVIUelsRmDXr0b9V6Ifu8E1GlCoH6zxYiSY8d5A==');
define( 'WP_ENVIRONMENT_TYPE', 'local' );
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
