<?php

  $to = 'shulenin_2005@mail.ru';


  $name = ClearData($_POST['name']);
  $email = ClearData($_POST['email']);
  $number = ClearData($_POST['subject']);
  $text = ClearData($_POST['message']);

  $mail -> isSMTP();
  $mail ->Host = 'smtp.mail.ru';
  $mail ->SMTPAuth = true;
  $mail ->Username = 'buisyguy@mail.ru';
  $mail ->Password = '$34fghjdrsewsavage';
  $mail ->SMTPSecure = 'ssl';
  $mail ->Port = 465;

  $mail ->setFrom('buisyguy@mail.ru');
  $mail ->addAddress('shulenin_2005@mail.ru');

  $mail ->isHTML(true);

  $mail->Subject = 'Заявка с сайта';
  $mail->Body = 'Имя ' . $name . '\r\n' . 'Номер телефона ' . $number . '\r\n' . 'Почта ' . $email . '\r\n' . $text;

  $mail -> AltBody = '';

  if (!mail -> send()) {
    echo 'Error';
  } else {
    header('location: thanks.html');
  }

?>
