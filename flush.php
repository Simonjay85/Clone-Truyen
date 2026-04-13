<?php
require_once('wp-load.php');
if ( ! current_user_can('manage_options') ) {
   wp_set_current_user(1);
}
flush_rewrite_rules(false);
echo "Rewrite rules flushed!";
