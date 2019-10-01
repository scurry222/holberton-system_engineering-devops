# changes a mistyped line in wordpress apache configuration
exec { 'wordpress hell':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin',
}
